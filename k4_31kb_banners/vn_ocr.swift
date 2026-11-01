import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count >= 2 else {
    fputs("Usage: vn_ocr <image_path>\n", stderr)
    exit(1)
}

let imagePath = CommandLine.arguments[1]
let url = URL(fileURLWithPath: imagePath)

guard let cgImageSource = CGImageSourceCreateWithURL(url as CFURL, nil),
      let cgImage = CGImageSourceCreateImageAtIndex(cgImageSource, 0, nil) else {
    fputs("Failed to load image: \(imagePath)\n", stderr)
    exit(2)
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true
request.recognitionLanguages = ["vi-VN", "en-US"]

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
do {
    try handler.perform([request])
    guard let observations = request.results else {
        print("[]")
        exit(0)
    }
    var out: [[String: Any]] = []
    for obs in observations {
        if let top = obs.topCandidates(1).first {
            let box = obs.boundingBox
            out.append([
                "text": top.string,
                "confidence": top.confidence,
                "bbox": [box.origin.x, box.origin.y, box.size.width, box.size.height]
            ])
        }
    }
    let data = try JSONSerialization.data(withJSONObject: out, options: [])
    if let jsonStr = String(data: data, encoding: .utf8) {
        print(jsonStr)
    }
} catch {
    fputs("OCR error: \(error)\n", stderr)
    exit(3)
}
