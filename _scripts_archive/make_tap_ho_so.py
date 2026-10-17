import markdown
import datetime

# Read template
with open("/Users/vietmac/Documents/CODE/k/temp_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Content
content_md = """
🔗 **Link bài viết (đã xuất bản):** [Bill Ackman: Kịch Bản Đầu Tư Ngược Đám Đông Xây Dựng Đế Chế 36 Tỷ Đô](https://vietndj.github.io/k/bill-ackman-kich-ban-dau-tu.html)

**TÓM TẮT 8 INSIGHT CỐT LÕI TỪ HỆ THỐNG:**

1. **Giới Hạn Quản Trị Rủi Ro & Lợi Thế Bất Đối Xứng:** Chỉ cược vào những ván bài rủi ro thấp nhất (có thể chịu đựng), nhưng tiềm năng thắng là vô cực (ví dụ vụ mua General Growth Properties).
2. **Nghệ Thuật Săn Thiên Nga Đen (Hedging):** Thủ sẵn bảo hiểm rủi ro để tạo dòng tiền khổng lồ đúng lúc đám đông hoảng loạn, sau đó dùng tiền đó gom tài sản giá rẻ (như các cú cược CDS năm 2008 và 2020).
3. **Đầu Tư Chủ Động (Activism):** Đừng thụ động chờ thị trường nhận ra giá trị doanh nghiệp. Hãy trực tiếp nhúng tay vào phòng họp hội đồng quản trị thay đổi CEO để ép thị trường phải định giá lại.
4. **Kiến Tạo Nguồn Vốn Vĩnh Cửu:** Khóa chặt nguồn vốn để loại bỏ hoàn toàn áp lực rút vốn ngắn hạn của cổ đông, cho phép đưa ra các quyết định dài hạn không bị cảm xúc chi phối.
5. **Đòn Bẩy Hệ Thống Khuyến Khích:** Mọi con người đều hành động theo incentives. Triệt tiêu cái tôi bằng cách loại bỏ P&L cá nhân, tất cả cùng ăn chia trên tổng danh mục chung (từ lễ tân đến quản lý quỹ).
6. **Chiến Lược Miễn Nhiễm FOMO Đám Đông:** Bỏ qua sự hào nhoáng bọt nước (AI, chip nhớ), tập trung mua những doanh nghiệp nhàm chán (bất động sản, bảo hiểm) nhưng có rãnh hào sâu không thể phá vỡ trong 10-20 năm tới.
7. **Giải Phẫu Sai Lầm Tàn Nhẫn:** Tỷ lệ thắng có thể chỉ 54% (như Roger Federer). Đừng cố gỡ gạc chỗ đã ngã, hãy tàn nhẫn cắt lỗ, giải phẫu dữ liệu sai lầm và chuyển vốn sang ván mới xác suất cao hơn.
8. **Chia Nhỏ Bức Tường Tuyệt Vọng:** Khi đối mặt khủng hoảng, đừng nhìn lên đỉnh núi huy hoàng quá khứ. Tập trung xử lý viên gạch ngay trước mặt hôm nay, sự tiến bộ sẽ tích lũy lãi kép dần dần.
"""

content_html = markdown.markdown(content_md)

# Wrap in a turn block
turns_html = f"""
<div id="turn-1" class="turn-block">
    <div class="turn-header agent">
        <div class="turn-role">Antigravity</div>
    </div>
    <div class="turn-content prose">
        {content_html}
    </div>
</div>
"""

takeaways_html = """
<li>Giới hạn rủi ro</li>
<li>Săn thiên nga đen</li>
<li>Đầu tư chủ động</li>
<li>Vốn vĩnh cửu</li>
"""

semantic_tags_html = """
<span class="vault-tag">#BillAckman</span>
<span class="vault-tag">#Investment</span>
"""

turn_pills = """<a href="#turn-1" class="toc-pill agent-pill">#1. Tóm Tắt Insight</a>"""
floating_nav = """<a href="#turn-1" class="f-link agent-link">#1. Tóm Tắt Insight</a>"""

out_html = template.format(
    title="Bill Ackman: 8 Insight Đầu Tư",
    clean_goal="Tóm tắt 8 insight cốt lõi từ podcast Bill Ackman",
    created_date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
    project="BILL ACKMAN",
    short_id="BA-8",
    total_turns="1",
    turn_pills=turn_pills,
    floating_nav_html=floating_nav,
    semantic_tags_html=semantic_tags_html,
    takeaways_html=takeaways_html,
    turns_html=turns_html
)

out_path = "/Users/vietmac/Desktop/Bill_Ackman_Tap_Ho_So.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out_html)

print("Đã tạo file:", out_path)
