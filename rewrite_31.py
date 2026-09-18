from bs4 import BeautifulSoup
import sys

file_path = "/Users/vietmac/Documents/CODE/k/logickenh-cac-trend-ap-dung-trong-lam-noi-dung-the-nao.html"

# Mảng 31 data
replacements = {
    "VỎ BỌC SỐ 1": {
        "title": "TREND #01: Vạch trần sai lầm thợ cũ (Vỏ: Đóng vai 'Luật sư' - Lõi: Khoe chuyên môn bắt bệnh)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là đóng vai người đi đòi lại công bằng, giải oan cho sự tự ti của khách. Lõi là chứng minh bạn am hiểu kỹ thuật sâu sắc đến mức chỉ nhìn là bắt trúng bệnh.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Giơ sản phẩm/hình ảnh bị hỏng lên. Câu đầu tiên: 'Đừng tự trách mình, không phải do cơ địa bạn đâu...'. Sau đó chỉ thẳng vào điểm làm ẩu của thợ cũ với thái độ điềm tĩnh, chuyên gia."
    },
    "VỎ BỌC SỐ 2": {
        "title": "TREND #02: Đọc vị nỗi sợ ngầm (Vỏ: Đi guốc trong bụng khách - Lõi: Khoe sự thấu cảm tinh tế)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là bóc trần những cái cớ 'bận, lười' khách hay nói. Lõi là để khách thấy bạn hiểu thấu nỗi sợ đau, sợ xấu, sợ mất tiền của họ, từ đó phát sinh niềm tin.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay góc POV (nhìn từ mắt mình) hoặc quay lén lúc đang tư vấn. 'Chị bảo bận không đi làm, thực ra em biết chị sợ làm xong bị sưng đúng không? Ở đây em dùng kỹ thuật...'."
    },
    "VỎ BỌC SỐ 3": {
        "title": "TREND #03: Cảnh báo 'Tiền mất tật mang' (Vỏ: Hù dọa nhẹ - Lõi: Khoe tư duy phòng bệnh)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là phân tích một ca hỏng nặng để cảnh báo. Lõi là chứng minh nếu khách làm ở bên bạn ngay từ đầu thì đã tiết kiệm được bao nhiêu tiền và thời gian.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Cầm hóa đơn hoặc kể một câu chuyện thiệt hại thực tế: 'Hôm nay nhận một ca sửa tốn gấp 3 lần tiền làm mới... Chỉ vì tháng trước tiếc rẻ không làm cái này'."
    },
    "VỎ BỌC SỐ 4": {
        "title": "TREND #04: Xoa dịu nỗi ám ảnh cũ (Vỏ: Bác sĩ tâm lý - Lõi: Khoe quy trình an toàn)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là nhắc lại trải nghiệm đau đớn/ám ảnh khách từng gặp. Lõi là show ra máy móc, quy trình êm ái của tiệm mình để dập tắt nỗi ám ảnh đó.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Ai từng bị... chắc chắn sẽ rất sợ bước này. Nhưng yên tâm, hãy nhìn cách bên mình làm...' (chèn đoạn B-roll quay thao tác siêu mượt và nhẹ nhàng)."
    },
    "VỎ BỌC SỐ 5": {
        "title": "TREND #05: Báo động đỏ (Vỏ: Thúc giục hành động - Lõi: Khoe giải pháp kịp thời)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là tạo ra một dead-line hoặc tình trạng khẩn cấp. Lõi là ép khách hàng không được trì hoãn và phải đặt lịch bên bạn ngay lập tức.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Nếu trên người bạn đang có dấu hiệu này, đừng để qua tuần sau...'. Đưa ra hậu quả nhãn tiền, sau đó chốt bằng nút CTA đặt lịch khám/tư vấn ngay."
    },
    "VỎ BỌC SỐ 6": {
        "title": "TREND #06: Pha 'Cứu nét' thần sầu (Vỏ: Giải cứu ca khó - Lõi: Khoe kỹ năng đỉnh cao)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là kịch tính hóa một ca cực khó tưởng chừng vô phương cứu chữa. Lõi là phô diễn tay nghề xuất chúng, giải quyết nhanh gọn lẹ.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Video có nhịp điệu nhanh. Bắt đầu bằng hình ảnh tồi tệ nhất. 'Ca này 3 tiệm chê, qua tay mình thì chỉ mất 30 phút...'. Tua nhanh quá trình làm (Timelapse) và bùm -> Kết quả hoàn hảo."
    },
    "VỎ BỌC SỐ 7": {
        "title": "TREND #07: Bác sĩ bắt mạch (Vỏ: Thần giao cách cảm - Lõi: Khoe kinh nghiệm nhìn là biết)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là màn biểu diễn 'đọc vị' tình trạng khách khi họ chưa kịp mở lời. Lõi là chứng minh kinh nghiệm dày dạn, làm hàng ngàn ca nên liếc qua là hiểu.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay lén hoặc đóng vai. Khách vừa bước vào: 'Chị không cần nói, em nhìn là biết chị dính lỗi này...'. Liệt kê 2-3 triệu chứng cực chuẩn khiến khách gật gù liên tục."
    },
    "VỎ BỌC SỐ 8": {
        "title": "TREND #08: Đuổi khách / Chê tiền (Vỏ: Ngông cuồng - Lõi: Khoe cái Tâm và tiêu chuẩn cao)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là từ chối phục vụ một khách hàng (có cầm tiền tới). Lõi là chứng minh bạn không thèm khát tiền đến mức làm bừa, chỉ nhận làm khi chắc chắn hiệu quả.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Hôm nay mình vừa từ chối làm cho một chị khách dù chị ấy nài nỉ... Lý do là vì tình trạng này có làm cũng không đẹp, tốn tiền vô ích. Cứ về nhà dưỡng trước...'."
    },
    "VỎ BỌC SỐ 9": {
        "title": "TREND #09: Ám ảnh cưỡng chế (Vỏ: Săm soi thái quá - Lõi: Khoe tính cẩn thận từng chi tiết)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là biến mình thành kẻ khó tính, kén cá chọn canh. Lõi là cho khách thấy sự tỉ mỉ, cầu toàn tuyệt đối trong từng khâu dịch vụ.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay cận cảnh macro. 'Nhiều người bảo mình bị điên khi soi từng milimet thế này... nhưng tính mình không ưng thì bắt làm lại bằng được mới thôi'."
    },
    "VỎ BỌC SỐ 10": {
        "title": "TREND #10: Bài học nhớ đời đền tiền (Vỏ: Bóc phốt chính mình - Lõi: Khoe sự uy tín, dám làm dám chịu)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là kể lại một tai nạn nghề nghiệp. Lõi là chứng minh bạn làm ăn đàng hoàng, không chối bỏ trách nhiệm, bồi thường sòng phẳng cho khách.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Ngồi tĩnh kể chuyện. 'Cách đây 2 năm, mình từng đền cho khách 50 triệu vì một sơ suất... Từ đó, toàn bộ quy trình ở tiệm mình phải siết lại như thế này...'."
    },
    "VỎ BỌC SỐ 11": {
        "title": "TREND #11: Cày cuốc xuyên đêm (Vỏ: Tiệm đông quá tải - Lõi: Khoe uy tín được khách tin yêu)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là than vãn sự vất vả, mệt mỏi. Lõi là tín hiệu xã hội ngầm: 'Tiệm mình siêu đông, khách tin tưởng giao phó đến mức phải làm ngoài giờ'.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay lúc 2h sáng, tiệm vẫn sáng đèn. Mặt thợ bơ phờ nhưng tay vẫn thoăn thoắt. 'Cám ơn các anh chị đã thương, 2h sáng vẫn ráng đợi em...'."
    },
    "VỎ BỌC SỐ 12": {
        "title": "TREND #12: Góc chill nịnh khách (Vỏ: Review đồ decor - Lõi: Khoe dịch vụ lấy khách làm trung tâm)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là quay một chi tiết nhỏ xinh xắn (ghế massage, trà ngon). Lõi là cho thấy bạn quan tâm đến trải nghiệm, chi tiêu hào phóng để chiều chuộng khách.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Đầu tư cái ghế này hết mấy chục triệu chỉ để khách ngồi chờ không bị đau lưng...'. Lấy điện thoại quay chậm lướt qua các tiện ích, nhạc lofi thư giãn."
    },
    "VỎ BỌC SỐ 13": {
        "title": "TREND #13: Nghiện dọn dẹp vô trùng (Vỏ: Cuộc chiến với vi khuẩn - Lõi: Khoe tiêu chuẩn an toàn y khoa)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là clip ASMR dọn dẹp, xịt khuẩn. Lõi là dập tắt nỗi sợ lây nhiễm, dơ bẩn của khách hàng kỹ tính.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay thao tác tháo lắp, lau chùi máy móc, ngâm đồ nghề vào cồn. Âm thanh cọ rửa rõ nét. 'Khách có thể không thấy, nhưng quy trình sát khuẩn nhà mình không bao giờ được phép tắt bước...'."
    },
    "VỎ BỌC SỐ 14": {
        "title": "TREND #14: POV: Khách VIP đi làm dịch vụ (Vỏ: Trải nghiệm người thứ nhất - Lõi: Review toàn cảnh tiệm)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là video dạng vlog 'Một ngày đi làm dịch vụ'. Lõi là để khách hàng hình dung trước chính xác họ sẽ được đối xử sướng như thế nào khi đến tiệm.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đặt camera ngang tầm mắt. Từ lúc đẩy cửa bước vào -> Lễ tân cười chào -> Nước uống bưng ra -> Thợ tư vấn nhẹ nhàng -> Nằm lên giường êm ái. Không cần nói, chỉ chèn text."
    },
    "VỎ BỌC SỐ 15": {
        "title": "TREND #15: ASMR chữa lành (Vỏ: Chỉ có âm thanh - Lõi: Khoe kỹ thuật điêu luyện mượt mà)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là sự thỏa mãn thính giác (tiếng kéo lách cách, tiếng nước chảy). Lõi là chứng tỏ đôi tay thợ rất nhịp nhàng, điêu luyện và sự thư giãn tuyệt đối của dịch vụ.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Dùng mic thu âm sát vào công cụ. Tuyệt đối không bật nhạc, không nói tiếng người. Focus hoàn toàn vào thao tác siêu mượt của đôi bàn tay."
    },
    "VỎ BỌC SỐ 16": {
        "title": "TREND #16: Chửi lính / Khắt khe với thợ (Vỏ: Đóng vai 'Ác' - Lõi: Khoe tiêu chuẩn khắt khe)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là sếp mắng nhân viên. Lõi là bảo vệ quyền lợi cho khách hàng, khẳng định tại đây không bao giờ có chuyện làm ẩu, làm cho xong.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay lén hoặc giả vờ quay lén. 'Bảo bao nhiêu lần rồi, bôi như thế này thì sao khách chịu nổi? Tháo ra làm lại ngay cho chị!'. Khách xem sẽ cực kỳ an tâm."
    },
    "VỎ BỌC SỐ 17": {
        "title": "TREND #17: Phản ứng bất ngờ của khách (Vỏ: Khách há hốc mồm - Lõi: Khoe kết quả siêu việt)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là reaction (phản ứng tự nhiên). Lõi là minh chứng chân thực nhất (Social Proof) thay vì tự mình khen mình.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đặt máy quay lén khoảnh khắc đưa gương cho khách xem kết quả cuối cùng. Bắt trọn nụ cười rạng rỡ, sự ngạc nhiên, tiếng thốt lên 'Wow, không nhận ra mình luôn'."
    },
    "VỎ BỌC SỐ 18": {
        "title": "TREND #18: Camera lén chăm sóc nửa đêm (Vỏ: Tình cảm mùi mẫn - Lõi: Khoe dịch vụ hậu mãi đỉnh cao)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là sự tận tâm. Lõi là chứng minh tiệm không 'đem con bỏ chợ', thu tiền xong vẫn lo lắng dặn dò khách từng chút một.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay màn hình tin nhắn lúc 11h đêm nhắn hỏi thăm khách, hoặc quay cảnh thợ cẩn thận ghi chép toa dặn dò dán lên túi thuốc mang về."
    },
    "VỎ BỌC SỐ 19": {
        "title": "TREND #19: Nhìn lại cái tiệm rách năm xưa (Vỏ: Hành trình vượt khó - Lõi: Khoe uy tín lâu năm vững bền)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là kể lể quá khứ bần hàn. Lõi là để khách thấy bạn có gốc rễ làm nghề lâu năm, đi lên bằng thực lực, đập tan định kiến 'bọn trẻ mới nổi trọc phú'.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Slide ảnh: 'Đây là tiệm mình 5 năm trước, cái ghế còn rách bươm... Còn đây là hiện tại, sau hàng ngàn khách hàng tin yêu ủng hộ...'."
    },
    "VỎ BỌC SỐ 20": {
        "title": "TREND #20: Giang tay chào đón đón khách (Vỏ: Nụ cười tỏa nắng - Lõi: Xóa bỏ sự xa cách, e ngại)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là tạo ra một visual thân thiện, hiếu khách. Lõi là phá vỡ bức tường tâm lý sợ bị chảnh, sợ bị vòi tiền của khách mới.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Chủ tiệm/Lễ tân mở cửa, mỉm cười cúi chào ống kính. 'Đừng ngại, cứ ghé qua bên mình kiểm tra miễn phí, không làm cũng không sao, được đón tiếp bạn là vui rồi!'."
    },
    "VỎ BỌC SỐ 21": {
        "title": "TREND #21: Đập hộp đồ nghề nghìn đô (Vỏ: Flex sương sương - Lõi: Khoe lợi thế cạnh tranh thiết bị xịn)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là review máy móc, hóa chất đắt tiền. Lõi là giải thích lý do 'Tại sao dịch vụ bên tôi lại đáng đồng tiền bát gạo', đập nát hàng chợ.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đập hộp lọ mực/cái máy xịn. 'Nhiều tiệm dùng hàng này (giơ hàng chợ) có 50k, còn bên mình nhập cây này (giơ hàng xịn) 5 củ... Lý do là để bảo vệ da cho khách.'."
    },
    "VỎ BỌC SỐ 22": {
        "title": "TREND #22: Đem người nhà ra làm chuột bạch (Vỏ: Tình cảm gia đình - Lõi: Khoe độ an toàn tuyệt đối 100%)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là làm đẹp cho mẹ, cho vợ. Lõi là bảo chứng rủi ro bằng không (Risk Free), vì chả ai dám đem đồ độc hại ra xài lên mặt mẹ ruột mình cả.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay cảnh thực hành trên mặt người nhà: 'Sản phẩm mới về, lôi ngay mẫu hậu ra test thử... Cái gì an toàn nhất mới dám xài cho mẹ, nên các chị em cứ yên tâm nhé!'."
    },
    "VỎ BỌC SỐ 23": {
        "title": "TREND #23: Tự đào lại clip trẻ trâu cũ (Vỏ: Tự bóc phốt mình - Lõi: Khoe sự lột xác tay nghề ngoạn mục)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là hài hước tự chê bản thân làm xấu ngày xưa. Lõi là để gián tiếp tát vào mặt những thợ kém cỏi hiện tại, đồng thời khẳng định tay nghề mình nay đã ở level chuyên gia.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Reaction cái video cũ: 'Trời ơi không hiểu sao 3 năm trước mình lại làm ra cái tác phẩm này... Nhìn lại bây giờ mới thấy sự thay đổi khủng khiếp ra sao...'."
    },
    "VỎ BỌC SỐ 24": {
        "title": "TREND #24: Xin lỗi, ở đây không bán rẻ (Vỏ: Tuyên ngôn chảnh - Lõi: Định vị phân khúc cao cấp, lọc tệp khách)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là thái độ bất cần, không chạy đua theo giá. Lõi là tiêm vào đầu khách hàng khái niệm: Của rẻ là của ôi, tiền nào của nấy.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Nhiều khách nhắn tin hỏi sao bên kia rẻ hơn một nửa... Dạ, em xin lỗi chứ ở đây tụi em thà vắng khách chứ không ép giá thợ để rồi làm ẩu cho anh chị đâu ạ'."
    },
    "VỎ BỌC SỐ 25": {
        "title": "TREND #25: Cúi đầu nhận lỗi công khai (Vỏ: Dũng cảm đối mặt phốt - Lõi: Khoe văn hóa chịu trách nhiệm, xử lý khủng hoảng đàng hoàng)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là chia sẻ về một đánh giá 1 sao. Lõi là lật ngược thế cờ, biến cái phốt thành cơ hội PR sự đàng hoàng, đền bù gấp đôi, bảo hành trọn đời.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> In luôn tờ giấy đánh giá 1 sao ra. 'Hôm nay tiệm nhận được feedback này... Mình hoàn toàn nhận lỗi và đây là cách tiệm bồi thường cho chị ấy... Cám ơn chị đã giúp tiệm tốt hơn'."
    },
    "VỎ BỌC SỐ 26": {
        "title": "TREND #26: Dỗ dành khách đang sốt ruột (Vỏ: Cuộc hội thoại hài hước - Lõi: Giải thích lý do phải làm kỹ, làm chậm)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là khách đang giục giã, cằn nhằn. Lõi là giáo dục khách hiểu rằng để có kết quả xịn thì không thể rút ngắn quy trình.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đóng vai trò chuyện: Khách: 'Làm nhanh lên em, 3 tiếng rồi'. Thợ: 'Chị ráng xíu nha, bước này mà làm tắt thì mai về nó bung bét hết, em thà chịu cực thêm 1 tiếng để chị đẹp cả tháng'."
    },
    "VỎ BỌC SỐ 27": {
        "title": "TREND #27: Vạch trần kỹ xảo ảo thuật (Vỏ: Bóc phốt thủ thuật - Lõi: Khoe kết quả của mình là chân thực)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là bóc mẽ cách các tiệm khác dùng app chỉnh sửa, góc sáng lừa tình. Lõi là khẳng định kết quả của tiệm bạn là cam thường, 100% người thật việc thật.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Quay clip chia đôi màn hình: 'Mọi người cứ thấy bóng loáng trên mxh là do họ dùng cái đèn chóa này và app này nè... Còn đây là cam thường tại tiệm mình, thật từ từng lỗ chân lông'."
    },
    "VỎ BỌC SỐ 28": {
        "title": "TREND #28: Lắc đầu từ chối ca nát (Vỏ: Thái độ rùng mình - Lõi: Dằn mặt khách ham rẻ, nâng tầm giá trị tiệm)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là ca thán về một hậu quả kinh dị do thợ khác để lại. Lõi là nhắc nhở khách hàng đừng vì ham rẻ mà chuốc họa, hãy giao phó cho người giỏi ngay từ đầu.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đeo găng tay, lắc đầu. 'Lại thêm một ca hỏng nát bét đi từ tiệm 199k qua kêu mình cứu. Thật sự ca này mình xin phép từ chối vì cấu trúc hỏng hoàn toàn rồi...'."
    },
    "VỎ BỌC SỐ 29": {
        "title": "TREND #29: Bắt đền thỏa thích (Vỏ: Ngông cuồng bảo hành - Lõi: Risk Reversal - Hủy diệt rủi ro cho khách)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là lời thách thức đanh thép. Lõi là đòn bẩy tâm lý cực mạnh (Risk Reversal), khách chốt sale ngay vì không còn bất kỳ sợ hãi nào.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> 'Ai nói làm xong không ưng ráng chịu? Ở đây làm xong soi gương không sướng, mình hoàn tiền 100% kèm trả luôn tiền xe cho bạn đi về. Uy tín chưa?'."
    },
    "VỎ BỌC SỐ 30": {
        "title": "TREND #30: Bóc giá gốc, phẫu thuật chi phí ẩn (Vỏ: Tự lật tẩy ngành - Lõi: Chứng minh sự minh bạch tuyệt đối)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là bảng liệt kê chi phí trần trụi. Lõi là đánh tan sự nghi ngờ 'bọn này chắc lời cắt cổ', chứng minh giá cao là do chi phí vật tư xịn.",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Cầm bảng viết phấn/giấy: 'Mọi người tưởng thu 1 triệu là mình đút túi hết à? Bóc giá cho xem: Tiền thuốc xịn 300k, khấu hao máy 200k, thợ chính 200k... Lãi có 100k thôi đó'."
    },
    "VỎ BỌC SỐ 31": {
        "title": "TREND #31: Giả vờ đuổi đi - Takeaway Close (Vỏ: Không màng chốt sale - Lõi: Thao túng tâm lý sợ bỏ lỡ FOMO)",
        "desc": "<strong>1. Tác dụng của Trend này:</strong> Vỏ là khuyên khách đừng làm vội, hãy về suy nghĩ. Lõi là tạo ra tâm lý khan hiếm, đảo ngược vị thế (khách phải theo đuổi mình).",
        "guide": "<strong>2. Hướng dẫn kịch bản quay:</strong> Đang tư vấn nửa chừng thì dừng lại: 'Chị ơi khoan làm, chị cứ về suy nghĩ kỹ đi hoặc đi tham khảo 3 tiệm nữa. Khi nào thật sự hiểu giá trị rồi hẵng quay lại em làm cho'."
    }
}

try:
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    # 1. Thêm khối NGỰA GỖ THÀNH TROY vào dưới doc-title
    h1 = soup.find("h1", class_="doc-title")
    if h1 and not soup.find(id="troy-horse"):
        intro_html = """
<div id="troy-horse" style="background: #eff6ff; border-left: 4px solid var(--cl-accent); padding: 24px 32px; border-radius: 0 12px 12px 0; margin-bottom: 40px;">
    <h3 style="margin-top:0; color: var(--cl-accent); font-family: var(--font-display-short); text-transform: uppercase; font-size: 18px; margin-bottom: 12px;">CHIẾN LƯỢC NGỰA GỖ THÀNH TROY: VỎ LÀ TREND - LÕI LÀ CHUYÊN MÔN</h3>
    <p style="margin-bottom: 12px;">Thuật toán mạng xã hội ưu tiên giải trí. Nếu bạn chỉ đứng nói đạo lý hoặc khoe máy móc, khán giả sẽ lướt qua trong 1 giây. Nếu bạn hùa theo trend nhảy múa, bạn có view rẻ tiền nhưng không bán được hàng.</p>
    <p style="margin-bottom: 12px;"><strong>Cách duy nhất để tạo LEAD:</strong> Dùng một cái "VỎ BỌC" mang tính giải trí, kịch tính, tò mò để dụ khán giả dừng lại xem. Sau khi họ đã cắn câu, bạn lặng lẽ tháo vỏ ra và đâm cái "LÕI" chuyên môn, tay nghề sắc bén của bạn vào não họ.</p>
    <p style="margin-bottom: 0;">Dưới đây là 31 chiếc "Vỏ bọc" hiệu quả nhất cho ngành dịch vụ Offline. Đừng copy mù quáng, hãy hiểu cơ chế VỎ - LÕI để tự linh hoạt cho ngành của mình.</p>
</div>
"""
        intro_soup = BeautifulSoup(intro_html, "html.parser")
        h1.insert_after(intro_soup)

    # 2. Vòng lặp đập đi xây lại 31 khối
    for h3 in soup.find_all("h3"):
        id_str = h3.get("id", "")
        if id_str.startswith("vo-boc-"):
            text = h3.get_text(strip=True)
            key = text.split(":")[0].strip() # VỎ BỌC SỐ 1
            if key in replacements:
                rep = replacements[key]
                # Đổi tên thẻ h3
                h3.string = rep["title"]
                
                # Tìm thẻ ul sát dưới h3
                ul = h3.find_next_sibling("ul")
                if ul:
                    lis = ul.find_all("li", recursive=False)
                    if len(lis) >= 3:
                        # Đập mục 1
                        lis[0].clear()
                        lis[0].append(BeautifulSoup(rep["desc"], "html.parser"))
                        # Đập mục 2
                        lis[1].clear()
                        lis[1].append(BeautifulSoup(rep["guide"], "html.parser"))
                        # Mục 3 (5 tiêu đề) giữ nguyên, có thể sửa chữ "3. 5 Tiêu đề:"
                        strong_title = lis[2].find("strong")
                        if strong_title:
                            strong_title.string = "3. Tiêu đề thực chiến (5 Ngành):"
                
    # Lưu lại file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print("SUCCESS")
except Exception as e:
    print("ERROR:", e)

