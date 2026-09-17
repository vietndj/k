import os
import glob
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup

def generate():
    files = glob.glob("*.html")
    exclude = ["index.html", "404.html", "rajchannel.html", "fix-url.html", "skills.html", "dom.html"]
    posts = []

    cover_mapping = {
        # Kịch bản offline (Mới nhất)
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-6.html": "https://media.fedu.vn/k_covers/cover_fb_ads_6_1789495461241.jpg",
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-5.html": "https://media.fedu.vn/k_covers/cover_fb_ads_5_1789495475061.jpg",
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-4.html": "https://media.fedu.vn/k_covers/cover_fb_ads_4_1789495486846.jpg",
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-3.html": "https://media.fedu.vn/k_covers/cover_no_customers_1789495449887.jpg",
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-2.html": "https://media.fedu.vn/k_covers/cover_offline_script_1789495439415.jpg",
        "kichbanoffline-phau-thuat-kich-ban-offline-phan-1.html": "https://media.fedu.vn/k_covers/cover_kich_ban_bds_1789517341819.jpg",
        "kichbanoffline-kich-ban-bds-30-phut-dap-tan-su-tri-hoan.html": "https://media.fedu.vn/k_covers/cover_kich_ban_bds_1789517341819.jpg",
        "kichbanoffline.html": "https://media.fedu.vn/k_covers/cover_offline_script_1789495439415.jpg",
        "kichbanoffline-kich-ban-08-chuyen-mon-vung-nhung-vang-khach.html": "https://media.fedu.vn/k_covers/cover_no_customers_1789495449887.jpg",
        "kichbanoffline-phan-tich-video-fb-ads-6.html": "https://media.fedu.vn/k_covers/cover_fb_ads_6_1789495461241.jpg",
        "kichbanoffline-phan-tich-video-fb-ads-5.html": "https://media.fedu.vn/k_covers/cover_fb_ads_5_1789495475061.jpg",
        "kichbanoffline-phan-tich-video-fb-ads-4.html": "https://media.fedu.vn/k_covers/cover_fb_ads_4_1789495486846.jpg",

        # 4 Bài Master Top Podcast (Studio 16:9 Bold Typography)
        "cong-thuc-1-kenh-de-phat-trien-podcast.html": "https://media.fedu.vn/k_covers/cover_growth_playbook.jpg",
        "so-tay-thuc-chien-khoi-nghiep-ky-nguyen-ai-podcast.html": "https://media.fedu.vn/k_covers/cover_khoi_nghiep_ai.jpg",
        "how-to-teach-and-grow-rich-business-model-podcast.html": "https://media.fedu.vn/k_covers/cover_day_hoc_lam_giau.jpg",
        "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.html": "https://media.fedu.vn/k_covers/cover_protocols_nao_bo.jpg",

        # 5 Bài Bối Cảnh Phòng Làm Việc Thực Tế (Home Workroom Anchor)
        "an-toan-ai-02-podcast.html": "https://media.fedu.vn/k_covers/cover_sieu_tri_tue.jpg",
        "hau-qua-cua-nhin-linh-tinh-science.html": "https://media.fedu.vn/k_covers/cover_khoa_hoc_than_kinh.jpg",
        "complex-5-anxiety-is-not-what-you-think.html": "https://media.fedu.vn/k_covers/cover_phuong_trinh_lo_au.jpg",
        "suyash-saraf-d2c-branding-gen-z-marketing-podcast.html": "https://media.fedu.vn/k_covers/cover_branding_trieu_do.jpg",
        "law-5-stress-is-not-what-happens-to-you.html": "https://media.fedu.vn/k_covers/cover_quy_tac_90_giay.jpg",

        # Nhóm bài chuyên sâu khác đã có ảnh R2
        "toi-uu-hieu-suat-nao-bo-suc-manh-nootropic-tu-creatine-va-che-do-an-thit-carnivore-dinh-cao-toi-gian-nang-luong-tu-joe-rogan-elon-musk.html": "https://media.fedu.vn/k_covers/toi_uu_hieu_suat_nao_bo_1789497940470.jpg",
        "su-giau-co-va-thanh-cong-tot-dinh-khong-bat-dau-tu-chien-thuat-kinh-doanh-hao-nhoang-ma-khoi-nguon-tu-nang-luc-quan-tri-tam-tri-ban-phai-thiet-ke-mot-moi-truong-khien-ky-luat-tro-nen-de-dang.html": "https://media.fedu.vn/k_covers/su_giau_co_va_thanh_cong_1789497961114.jpg",
        "no-den-tu-long-dung-cam-dam-lam-ra-nhung-video-toi-te-ban-dau-kien-tri-cai-thien-1-moi-ngay-va-tap-trung-phuc-vu-sau-sac-cho-nhom-khan-gia-ngach-dang-chiu-chung-noi-dau-ma-ban-tung-vuot-qua-podcast.html": "https://media.fedu.vn/k_covers/no_den_tu_long_dung_cam_1789497983814.jpg",
        "be-khoa-thuat-toan-xay-kenh-niche-podcast.html": "https://media.fedu.vn/k_covers/be_khoa_thuat_toan_1789498007808.jpg",
        "nghe-thuat-chuyen-minh-10-nam-dam-phan-hop-dong-molly-mcadam-podcast.html": "https://media.fedu.vn/k_covers/nghe_thuat_chuyen_minh_1789498030877.jpg",
        "co-the-ban-khong-he-ghet-ban-no-chi-dang-lam-xuat-sac-nhiem-vu-sinh-ton-bang-cach-bat-che-do-khang-cu-lai-su-sut-giam-calo-trong-mot-the.html": "https://media.fedu.vn/k_covers/co_the_ban_khong_he_ghet_1789498064292.jpg",
        "giac-ngu-hieu-suat-dinh-cao-science-long-form.html": "https://media.fedu.vn/k_covers/giac_ngu_hieu_suat_dinh_cao_1789498074896.jpg",
        "dr-v-mohan-diabetes-sugar-genetics-health-podcast.html": "https://media.fedu.vn/k_covers/dr_v_mohan_diabetes_1789498087376.jpg",
        "su-thay-doi-khong-den-tu-viec-tim-kiem-mot-cuoc-song-de-dang-hon-ma-den-tu-viec-chu-dong-lua-chon-nhung-kho-khan-co-chu-dich-ap-luc-khong.html": "https://media.fedu.vn/k_covers/su_thay_doi_khong_den_tu_1789498100264.jpg",
        "mat-ma-cua-su-loi-cuon-podcast-science.html": "https://media.fedu.vn/k_covers/mat_ma_cua_su_loi_cuon_1789498111501.jpg",
        "co-hoc-luong-tu-va-truc-giac-tam-linh.html": "https://media.fedu.vn/k_covers/co_hoc_luong_tu_1789498159596.jpg",
        "dr-joe-dispenza-rewire-brain-neuroplasticity-fear-podcast.html": "https://media.fedu.vn/k_covers/dr_joe_dispenza_1789498172191.jpg",
        "hanh-trinh-khai-mo-sang-tao-chua-lanh-noi-dau-podcast.html": "https://media.fedu.vn/k_covers/hanh_trinh_khai_mo_1789498182380.jpg",
        "hanh-trinh-hack-nao-bo-science.html": "https://media.fedu.vn/k_covers/hanh_trinh_hack_nao_bo_1789498197546.jpg",
        "chung-ta-khong-phai-la-nhung-co-may-thuan-ly-tri-co-the-thoat-khoi-quy-luat-sinh-hoc-con-nguoi-hien-dai-dang-van-hanh-bang-he-dieu-hanh-cua-to-tien-tren-thao-nguyen-podcast-science.html": "https://media.fedu.vn/k_covers/chung_ta_khong_phai_1789498209355.jpg",
        "tamlyhoc-tam-ly-phong-thu-cua-nguoi-mua.html": "https://media.fedu.vn/k_covers/tamlyhoc_tam_ly_phong_thu_1789498264428.jpg",
        "he-thong-phuc-hop-prompt-4-giai-ma-ban-chat-he-dieu-hanh-vu-tru-va-kien-truc-nhan-thuc-bac-cao.html": "https://media.fedu.vn/k_covers/he_thong_phuc_hop_1789498278127.jpg",
        "tu-duy-van-hanh-cua-ceo-uber-science.html": "https://media.fedu.vn/k_covers/tu_duy_van_hanh_1789498289898.jpg",
        "giai-phong-tam-tri-tu-co-the-podcast.html": "https://media.fedu.vn/k_covers/giai_phong_tam_tri_1789498301154.jpg",
        "dai-chien-tu-duy-tranh-luan-nay-lua-giua-kevin-oleary-cenk-uygur-ve-tac-dong-cua-ai-den-that-nghiep-cuoc-dua-dia-chinh-tri-my-trung-va.html": "https://media.fedu.vn/k_covers/dai_chien_tu_duy_1789498312827.jpg",
        "xay-kenh-tam-ly-sang-tao-bai-hoc-tu-theo-von-fiona-cauley-science-podcast.html": "https://media.fedu.vn/k_covers/poster_the_godfather_1789519978150.jpg",
        "satinder-sartaaj-sufi-music-culture-fame-podcast.html": "https://media.fedu.vn/k_covers/poster_the_matrix_1789519988925.jpg",
        "dan-martell-ai-strategy-for-entrepreneurs-podcast.html": "https://media.fedu.vn/k_covers/poster_fight_club_1789520001215.jpg",
        "andrew-huberman-daily-habits-neuroscience-podcast.html": "https://media.fedu.vn/k_covers/poster_the_dark_knight_1789520014371.jpg",
        "masterclass-giai-ma-suc-khoe-sinh-ly-khoai-cam-nu-dr-rachel-rubin-podcast.html": "https://media.fedu.vn/k_covers/poster_inception_1789520026980.jpg",
        "tuoi-30-khong-phai-la-luc-ban-bat-dau-gia-di-ma-la-thoi-diem-moi-thoi-quen-cua-ban-bat-dau-tinh-lai-kep-podcast.html": "https://media.fedu.vn/k_covers/poster_raiders_lost_ark_1789520048668.jpg",
        "ngu-day-chay-nuoc-mui-science.html": "https://media.fedu.vn/k_covers/poster_terminator_2_1789520060665.jpg",
        "su-tai-sinh-thuc-su-khong-bao-gio-bat-dau-bang-viec-co-gang-va-viu-lai-phien-ban-cu-no-bat-dau-bang-long-dung-cam-de-chon-vui-nhung-lop-vo.html": "https://media.fedu.vn/k_covers/poster_interstellar_1789520072418.jpg",
        "toan-hoc-va-dau-tu-1-science.html": "https://media.fedu.vn/k_covers/poster_forrest_gump_1789520082263.jpg",
        "get-rich-off-salary-money-masterclass-podcast.html": "https://media.fedu.vn/k_covers/poster_john_wick_1789520096603.jpg",
        "tien-bac-chi-tieu-podcast.html": "https://media.fedu.vn/k_covers/poster_gladiator_1789520121636.jpg",
        "toi-uu-ram-nho-05-nhom-4-mo-van-sang-tao-sau-nap-du-lieu-science.html": "https://media.fedu.vn/k_covers/poster_top_gun_1789520131570.jpg",
        "oi-uu-ram-nho-03-nhom-2-van-hanh-trong-ngay-science.html": "https://media.fedu.vn/k_covers/poster_mad_max_fury_road_1789520142924.jpg",
        "gioi-han-cua-y-chi-nguoi-quan-tuong-03-spiritual-science.html": "https://media.fedu.vn/k_covers/poster_iron_man_1789520154437.jpg",
        "cach-hoc-that-tu-insta-science.html": "https://media.fedu.vn/k_covers/poster_blade_runner_2049_1789520168852.jpg",
        "ban-khong-the-kien-tao-mot-cuoc-doi-co-y-nghia-bang-hanh-phuc-hoi-hot-hay-viec-dong-vai-nan-nhan-science.html": "https://media.fedu.vn/k_covers/poster_pulp_fiction_1789520201983.jpg",
        "nang-luc-cat-bo-bot-cac-lop-dinh-danh-ao-science.html": "https://media.fedu.vn/k_covers/poster_shawshank_redemption_1789520212701.jpg",
        "ham-luoi-mat-tay-tho-02-science.html": "https://media.fedu.vn/k_covers/poster_star_wars_1789520223562.jpg",
        "law-4-ai-made-iq-and-eq-accessible.html": "https://media.fedu.vn/k_covers/poster_mission_impossible_1789520233409.jpg",
        "giai-ma-su-chan-thuc-kien-truc-noi-dung-podcast.html": "https://media.fedu.vn/k_covers/poster_truman_show_1789520245491.jpg",
        "mokksh-sani-liquor-retail-business-economics-podcast.html": "https://media.fedu.vn/k_covers/poster_lord_of_the_rings_1789520282828.jpg",
        "kiem-soat-insulin-science.html": "https://media.fedu.vn/k_covers/poster_v_for_vendetta_1789520322141.jpg",
        "khong-phai-la-nham-mat-kien-tri-ma-la-su-kien-tri-thu-nghiem-lien-tuc-podcast.html": "https://media.fedu.vn/k_covers/poster_titanic_1789520348688.jpg",
        "chua-lanh-dua-tre-ben-trong-podcast.html": "https://media.fedu.vn/k_covers/poster_silence_of_the_lambs_1789520360430.jpg",
        "kien-truc-thuc-tai-buc-man-ao-giac-science.html": "https://media.fedu.vn/k_covers/poster_back_to_the_future_1789520446245.jpg",
        "sell-your-knowledge-make-money-online-podcast.html": "https://media.fedu.vn/k_covers/poster_harry_potter_1789520534828.jpg",
        "su-thuc-tinh-ky-nguyen-ai-mentor-insight-podcast.html": "https://media.fedu.vn/k_covers/poster_cast_away_1789520547871.jpg",
        "ganh-nang-cua-su-dang-do-science.html": "https://media.fedu.vn/k_covers/poster_drive_1789520559001.jpg",
        "hanh-trinh-thuc-tinh-nhe-nhang-podcast.html": "https://media.fedu.vn/k_covers/poster_catch_me_if_you_can_1789520567656.jpg",

        # 30 Movie Poster AI Covers
        "dung-cho-doi-dong-luc-vi-no-la-mot-loi-noi-doi-su-thay-doi-thuc-su-chi-bat-dau-khi-ban-ep-ban-than-hanh-dong-truoc-khi-cam-xuc-kip-len.html": "https://media.fedu.vn/k_covers/poster_jurassic_park_1789521024715.jpg",

        # 30 Movie Poster AI Covers
        "brilliant-content-ideas-easier-than-ai-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_scarface.jpg",
        "sieu-tri-tue-asi-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_oppenheimer.jpg",
        "hanh-trinh-tim-kiem-ban-doi-loi-giai-tu-noi-tam-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dune_two.jpg",
        "giai-ma-tuoi-tho-dinh-duong-thuc-vat-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_space_odyssey.jpg",
        "khai-phong-tiem-nang-sang-tao.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_shining.jpg",
        "bi-quyet-giu-chan-nguoi-xem-trong-3-giay-dau-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_taxi_driver.jpg",
        "thien-boc-dong-va-hieu-suat-cong-viec.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_kill_bill.jpg",
        "10m-ceo-why-ceos-need-personal-brand-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_blade_runner.jpg",
        "5-danh-muc-quay-pho-bien.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_apocalypse_now.jpg",
        "so-tay-sinh-ton-ky-nguyen-ai-2026-2027-mo-gawdat-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_goodfellas.jpg",
        "he-thong-phan-bo-dong-tien-chan-dung-ro-ri-cam-xuc-hay-khong-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_spider_man.jpg",
        "bi-quyet-tu-tin-camera.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_wolf_wall_street.jpg",
        "vanessa-van-edwards-nghe-thuat-ket-noi-giao-tiep-dinh-cao-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_avengers_endgame.jpg",
        "giai-ma-y-nghia-cuoc-song-cai-chet.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_django_unchained.jpg",
        "hanh-trinh-chua-lanh-khoi-sinh-tu-bong-toi-macklemore-science-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_casino_royale.jpg",
        "98-founder-dang-tu-giam-minh-trong-mot-nha-tu-tra-luong-cao-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_rocky.jpg",
        "kien-truc-toi-uu-hoa-nao-bo-hanh-vi-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_braveheart.jpg",
        "hanh-trinh-tinh-thuc-kham-pha-ban-nga-loi-giai-tu-mooji-ve-tinh-yeu-tinh-thuc-ru-bo-chap-niem-va-danh-thuc-ngon-lua-tri-tue-ben-trong-ban.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_saving_private_ryan.jpg",
        "tai-sao-giay-but-danh-bai-ban-phim-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_prestige.jpg",
        "so-tay-tri-thuc-song-khong-hoi-tiec-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_shutter_island.jpg",
        "ngung-do-loi-cho-gen-xau-hay-so-phan-moi-roi-loan-tam-ly-tu-tram-cam-lo-au-adhd-den-tu-ky-ve-ban-chat-sau-xa-nhat-deu-la-roi-loan-chuyen.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_no_country_old_men.jpg",
        "real-youtube-advice-for-real-entrepreneurs-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_movie_1917.jpg",
        "meylin-va-66-ngay-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_revenant.jpg",
        "ban-dang-bi-dieu-khien-boi-chinh-cam-xuc-cua-minh-su-khac-biet-giua-nguoi-lam-chu-cuoc-choi-va-ke-bi-thao-tung-nam-o-cho-ke-bi-thao-tung.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_alien.jpg",
        "life-knowledge-02-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_whiplash.jpg",
        "tri-tue-ngan-nam-cua-thieu-lam-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_parasite.jpg",
        "thay-doi-thoi-quen-ket-luan-chi-quan-sat.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_leon_professional.jpg",
        "viec-dat-muc-tieu-chi-cho-rieng-minh-mua-nha-co-6-mui-vo-dich-la-mot-tro-choi-huu-han-choi-xong-la-tram-cam-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_grand_budapest.jpg",
        "fastest-way-to-monetize-content-longform-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_road_warrior.jpg",
        "tai-sao-ko-xem-truoc-2h15-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_clockwork_orange.jpg",
        "chien-luoc-su-nghiep-top-1-tuyen-dung-ky-nguyen-ai-silicon-valley-girl.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_eternal_sunshine.jpg",
        "su-troi-day-cua-y-thuc-may-moc-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_platoon.jpg",
        "hanh-trinh-tam-linh-spiritual.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_die_hard.jpg",
        "tim-hieu-o-cung-hagibis-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_big_lebowski.jpg",
        "so-tay-co-van-xay-dung-doanh-nghiep-ai-first-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ghostbusters.jpg",
        "hammat-vai-ban-tay-mo-ho-tro-thien-dinh-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_american_psycho.jpg",
        "moi-doanh-nghiep-that-bai-trong-viec-chot-sale-vi-mac-benh-ai-ky-thich-noi-ve-su-menh-cua-minh-thay-vi-giai-quyet-noi-dau-dang-chay-mau-cua-khach-hang-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_departed.jpg",
        "landing-page-giai-ma-hanh-vi-loi-ich-vo-ly-02-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_skyfall.jpg",
        "hanh-trinh-chua-lanh-tai-sinh-science-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_great_gatsby.jpg",
        "behavior-discipline-architecture-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ex_machina.jpg",
        "ban-chat-cua-cam-nhan-thien-nhien-02.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dune_one.jpg",
        "88-dan-so-dang-hong-he-thong-trao-doi-chat-tu-ben-trong-chia-khoa-khong-phai-la-tinh-calo-hay-chay-bo-ma-la-ngung-nap-thuc-pham-sieu-che.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_se7en.jpg",
        "nang-luong-song-qua-quan-sat.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_snatch.jpg",
        "amcc-book-typo.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_tron_legacy.jpg",
        "prashant-desai-protein-metabolic-health-muscle-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_batman.jpg",
        "kichbanoffline-01-vuong-the-dien-truoc-ong-kinh.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_blade.jpg",
        "complex-8-the-skill-you-need-agility.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_children_of_men.jpg",
        "sales-khong-phai-la-thao-tung-no-la-quyen-luc-mem-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_speed.jpg",
        "5-nganh-nghe-bien-mat-khi-ai-tang-toc.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_edge_of_tomorrow.jpg",
        "troi-buoc-tien-hoa-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_constantine.jpg",

        # 30 Movie Poster AI Covers
        "deepthink-03-podcast-dashboard-science-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_good_bad_ugly.jpg",
        "thanh-cong-tot-dinh-khong-den-tu-viec-sao-chep-nhung-ke-dung-dau-ma-den-tu-viec-ban-kien-nhan-chiu-dung-su-nhat-nheo-trong-bong-toi-suot.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_once_upon_hollywood.jpg",
        "how-to-make-100k-selling-your-knowledge-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_joker_2019.jpg",
        "ashwin-srivastava-harvard-mba-frameworks-career-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_american_beauty.jpg",
        "nghe-thuat-cua-nhung-quyet-dinh-vi-dai-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_jaws.jpg",
        "fix-this-core-bottleneck-business-success-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_psycho.jpg",
        "dr-k-relationship-psychology-trauma-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_vertigo.jpg",
        "noi-dau-va-nhung-goc-toi-tam-nhat-cua-con-nguoi-khong-phai-la-thu-de-choi-bo-no-la-canh-cua-bat-buoc-phai-di-qua-de-dat-duoc-su-thuc-tinh.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_rear_window.jpg",
        "99-percent-online-businesses-replaced-content-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_sixth_sense.jpg",
        "giai-ma-ap-luc-nuoi-day-con-thanh-cong-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_memento.jpg",
        "hack-tien-hoa-toi-uu-nao-spiritual.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_reservoir_dogs.jpg",
        "cach-kiem-soat-khung-hinh-khi-quay-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_inglourious_basterds.jpg",
        "thiet-ke-cuoc-song-phong-phu-khong-can-phai-tan-tien-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_social_network.jpg",
        "tamlyhoc-18-phan-xa-giu-the-dien.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_la_la_land.jpg",
        "giai-ma-tam-thuc-7-nguyen-tac-hermetic-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_her_movie.jpg",
        "life-knowledge-01-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_arrival.jpg",
        "gut-health-masterclass-giai-ma-he-vi-sinh-duong-ruot-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_district_9.jpg",
        "thuat-toan-trieu-view-shorts-mathis-bolt-motiversity-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_fifth_element.jpg",
        "buoi-sang-khong-phai-la-luc-bat-dau-ngay-moi-no-la-luc-lap-trinh-he-dieu-hanh-cho-bo-nao-neu-ban-khong-chu-dong-viet-kich-ban-cho-tam-tri-su-lo-au-qua-khu-va-mang-xa-hoi-se-tu-dong-viet-thay-ban-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_total_recall.jpg",
        "suc-manh-cua-su-buong-bo-podcast-spiritual.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_minority_report.jpg",
        "system-intelligence-architect-mo-gawdat.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_i_am_legend.jpg",
        "thien-di-dao-va-tieu-hoa-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_terminator_1.jpg",
        "so-tay-trieu-do-khoi-nghiep-ky-nguyen-moi-cung-chu-tich-shopify-science-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_predator.jpg",
        "lakshya-sen-olympic-champion-mindset-resilience-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_aliens_1986.jpg",
        "dung-viet-blog-nua-hay-xay-co-may-media-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_robocop.jpg",
        "tam-tri-khong-phai-la-mot-chiec-binh-de-cho-sut-me-theo-thoi-gian-no-la-mot-co-bap-it-nhat-45-den-70-cac-ca-sa-sut-tri-tue-dementia-hoan.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_thing.jpg",
        "thien-it-dan-den-su-boc-dong.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_halloween.jpg",
        "lam-chu-tam-tri-ky-luat-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_nightmare_elm_street.jpg",
        "tai-sao-but-giay-danh-bai-ban-phim-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_friday_the_13th.jpg",
        "giu-cho-duong-cong-glucose-cua-ban-phang-lang-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_exorcist.jpg",
        "imtiaz-ali-filmmaking-storytelling-heartbreak-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_rosemarys_baby.jpg",
        "thuong-hieu-ca-nhan-la-he-dieu-hanh-cua-doanh-nghiep-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_black_swan.jpg",
        "chung-ta-dang-song-trong-mot-thoi-dai-bi-thao-tung-boi-marketing-thuc-pham-chia-khoa-vang-khong-nam-o-viec-nap-that-nhieu-protein-hay-am.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_requiem_for_a_dream.jpg",
        "trang-thai-co-the-quyet-dinh-suy-nghi-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_trainspotting.jpg",
        "ao-anh-cua-su-ham-muon.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_fargo.jpg",
        "giai-ma-ton-thuong-tam-ly-dr-gabor-mate-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_true_grit.jpg",
        "giai-ma-tuong-lai-cung-sam-altman-patrick-collison-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_hateful_eight.jpg",
        "complex-4-mo-gawdat-the-skill-you-need-in-the-age-of-ai.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_once_upon_america.jpg",
        "giai-ma-he-vi-sinh-duong-ruot-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_heat_1995.jpg",
        "su-tien-hoa-he-sinh-thai-moi-elon-musk-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_collateral.jpg",
        "kha-nang-tao-ra-khong-gian-an-toan-cho-minh-va-nguoi-khac-dung-khi-de-the-hien-con-nguoi-that-dau-tien-va-nghe-thuat-bien-nhung-tuong-tac-nhat-nheo-thanh-co-hoi-ket-noi-sau-sac-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_casino_1995.jpg",
        "nghien-ngap-khong-phai-la-su-yeu-kem-ve-y-chi-ma-la-dau-hieu-cho-thay-nao-bo-dang-bi-doi-nhung-ket-noi-thuc-su-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_raging_bull.jpg",
        "su-giai-phong-kinh-te-cua-phu-nu-la-mot-thanh-tuu-vi-dai-nhung-no-da-xe-bo-kich-ban-song-truyen-thong-cua-dan-ong-vai-tro-tru-cot-ma-chua-he-viet-lai-mot-kich-ban-moi-dan-ong-khong-doc-hai-ho-dang-roi-vao-khung-hoang-cua-su-vo-dung-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_irishman.jpg",
        "nghe-thuat-thu-nghiem-nhanh-hang-tram-y-tuong-toi-voi-gia-re-mat-dep-bo-cai-toi-de-nhuong-cho-cho-nguoi-gioi-hon-va-giu-ky-luat-thep-voi-ranh-gioi-cuoc-song-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_uncut_gems.jpg",
        "troi-buoc-porn-other-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_eeaao.jpg",
        "khai-pha-suc-manh-sinh-hoc-tam-thuc-tai-lap-trinh-tiem-thuc-nho-ban-thiet-ke-epigenetics-va-tan-so-trai-tim-de-thiet-ke-so-phan-thien-duong.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_babylon_2022.jpg",
        "frank-walliser-bentley-luxury-automotive-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_birdman.jpg",
        "giai-ma-spotify-tu-duy-cua-mot-ceo-huong-noi-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_grandmaster.jpg",
        "wtf-is-wealth-ray-dalio-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_crouching_tiger.jpg",
        "giai-ma-tam-thuc-tu-day-vuc-den-trieu-phu-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_hero_2002.jpg",

        # 30 Movie Poster AI Covers
        "suc-manh-cua-su-gioi-han-david-epstein-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_enter_the_dragon.jpg",
        "richard-teng-binance-crypto-future-of-money-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ip_man.jpg",
        "tri-tue-he-thong-prompt-1-bao-cao-co-hoc-dong-luc-hoc-hanh-vi.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_oldboy.jpg",
        "ankur-warikoo-fake-life-money-psychology-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_memories_of_murder.jpg",
        "ban-khong-can-yeu-100-cong-viec-chi-can-20-la-du-de-tao-ra-phep-mau-mien-nhiem-voi-su-kiet-suc-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_handmaiden.jpg",
        "suc-khoe-doi-ban-chan-chinh-la-nen-mong-cho-kha-nang-van-dong-va-su-truong-tho-cua-toan-bo-co-the-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_train_to_busan.jpg",
        "ngoi-chan-moi-co-dong-luc-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_snowpiercer.jpg",
        "lap-trinh-bo-nao-01-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_mad_max_1979.jpg",
        "dr-viju-jacob-spice-empire-fmcg-business-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_furiosa.jpg",
        "ky-luat-khong-phai-la-su-ep-buoc-dau-kho-ma-la-qua-trinh-thiet-ke-mot-he-thong-moi-truong-va-thoi-quen-sao-cho-viec-lam-dieu-dung-dan-tro.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_road.jpg",
        "complex-6-the-3-questions-that-end-unhappiness.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_quiet_place.jpg",
        "vo-hieu-hoa-lo-hong-y-chi-bang-tu-dong-hoa-tai-chinh-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_get_out.jpg",
        "giai-ma-he-sinh-thai-duong-ruot-bo-nao-thu-hai-cua-co-the-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_us_movie.jpg",
        "myron-golden-first-million-charge-premium-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_midsommar.jpg",
        "empire-of-ai-kien-truc-du-lieu-rang-buoc-he-thong-myth-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_hereditary.jpg",
        "hanh-vi-cuong-che-va-loi-the-nao-bo-spiritual-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_lighthouse.jpg",
        "chung-ta-khong-benh-vi-thieu-protein-hay-an-theo-che-do-low-fat-chung-ta-benh-vi-he-thong-cong-nghiep-thuc-pham-da-thao-tung-tam-ly-bien.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_witch.jpg",
        "giai-ma-luat-cua-mot-tam-thuc-khai-sang-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_northman.jpg",
        "tinh-yeu-va-hon-nhan-khong-phai-la-mot-mon-qua-vinh-vien-chung-la-mot-khoan-vay-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_pans_labyrinth.jpg",
        "giai-ma-nghe-podcast-sang-tao-noi-dung.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_shape_of_water.jpg",
        "su-phan-nan-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_hellboy.jpg",
        "su-thay-doi-mang-tinh-buoc-ngoat-paradigm-shift-khong-den-tu-viec-ban-hieu-van-de-cua-minh-ma-den-tu-viec-ban-co-dam-buoc-ra-khoi-con-nghien-hoa-hoc-do-chinh-nhung-cam-xuc-dau-kho-trong-qua-khu-tao-ra-hay-khong-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_pacific_rim.jpg",
        "dieu-huong-dopamine-deepthink-01-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_godzilla.jpg",
        "bo-nao-la-co-quan-ra-quyet-dinh-va-hinh-thanh-nhan-cach-cua-ban-khi-nao-hoat-dong-dung-ban-song-dung-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_king_kong.jpg",
        "discipline-architecture-2026-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_casablanca.jpg",
        "kinh-nguyet-la-mot-sinh-hieu-quan-trong-vital-sign-estrogen-va-progesterone-khong-chi-la-hormone-gioi-tinh-chung-la-nen-tang-dieu-khien-cau-truc-nao-bo-mat-do-xuong-va-suc-khoe-trao-doi-chat-cua-ban-suot-cuoc-doi-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dawn_planet_apes.jpg",
        "dopamine-architecture-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_chinatown.jpg",
        "su-tinh-thuc-dong-chay-thinh-vuong-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_aquaman.jpg",
        "doi-dien-bong-toi-dinh-hinh-lai-ky-luat-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_amadeus.jpg",
        "architecture-of-intelligence-mo-gawdat.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_full_metal_jacket.jpg",
        "jasmine-star-build-brand-automate-trust-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_big_lebowski.jpg",
        "su-cao-chung-cua-lao-dong-nhan-thuc-co-hoi-5050-cho-nhan-loai-science-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_citizen_kane.jpg",
        "giai-ma-suc-khoe-toan-dien-landing-page-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_seven_samurai.jpg",
        "rajshamani-21-podcasts-hub.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ran.jpg",
        "khoa-hoc-toi-uu-hoa-nhan-thuc-can-thiep-than-kinh-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_stalker.jpg",
        "personal-brand-blueprint-film-everything-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_watchmen.jpg",
        "nao-bo-va-viec-chan-nan-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_sin_city.jpg",
        "the-one-skill-needed-to-make-millions-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_movie_300.jpg",
        "faith-and-wealth-spiritual-business-principles-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_troy.jpg",
        "moi-thanh-bai-trong-cuoc-doi-ban-khong-nam-o-ngoai-canh-ma-duoc-quyet-dinh-boi-3-truc-lam-chu-chinh-minh-quan-sat-sac-ben-va-giao-tiep-thau-cam-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_kingdom_of_heaven.jpg",
        "kichbanoffline-khi-nguoi-co-nghe-tu-tua-vao-huu-xa-tu-nhien-huong.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_last_samurai.jpg",
        "ban-hang-la-ky-nang-song-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_master_commander.jpg",
        "kien-tao-the-gioi-moi-charles-eisenstein-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_pirates_caribbean.jpg",
        "su-phi-ly-khi-lam-mot-con-nguoi-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_indiana_last_crusade.jpg",
        "how-to-become-a-millionaire-start-teaching-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_national_treasure.jpg",
        "omarchannel.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_da_vinci_code.jpg",
        "su-that-ve-anh-sang-y-sinh-hoc-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_sherlock_holmes.jpg",
        "kichbanoffline-dong-goi-bai-tu-van-thanh-video-1-phut.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_tenet.jpg",
        "deepak-sahni-health-gut-liver-longevity-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dunkirk.jpg",
        "ban-khong-he-hong-hoc-ban-chi-dang-can-kiet-nguyen-lieu-de-van-hanh-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_aviator.jpg",

        # 30 Movie Poster AI Covers
        "kenh.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_empire_strikes_back.jpg",
        "tai-sao-ban-lai-giam-iq-khi-co-tiet-kiem-bac-le-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_big_short.jpg",
        "nhin-mat-tre-em-va-nguoi-lon-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_matrix_reloaded.jpg",
        "giai-ma-tinh-yeu-dich-thuc-nghe-thuat-chua-lanh.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_pirates_dead_mans_chest.jpg",
        "giai-ma-tam-tri-loi-thoat-cho-mot-the-he-co-don-nghien-ngap-dr-k-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_twelve_angry_men.jpg",
        "mark-manson-psychology-of-love-toxic-relationships-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_casablanca_1942.jpg",
        "architecture-of-an-ai-native-generation.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_lawrence_of_arabia.jpg",
        "law-7-ai-made-iq-and-eq-accessible.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_rashomon.jpg",
        "performance-10-the-real-danger-of-ai.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_sunset_boulevard.jpg",
        "ao-giac-nang-luc-khoa-hoc-cua-su-thuc-hanh-podcast-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_third_man.jpg",
        "ky-nguyen-abundance-tu-do-cong-nghe-giai-ma-elon-musk-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_north_by_northwest.jpg",
        "tri-tue-ban-dia-siberi-snow-raven.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dial_m_for_murder.jpg",
        "masterclass-giai-phau-ma-tran-ky-luat-thep-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_chinatown_1974.jpg",
        "ban-khong-beo-vi-thieu-y-chi-ban-dang-bi-hack-nao-bo-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_la_confidential.jpg",
        "david-eagleman-nao-bo-khong-phai-la-mot-co-may-co-dinh-ma-la-mot-he-sinh-thai-khong-ngung-tai-cau-truc-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_french_connection.jpg",
        "danh-thuc-niem-vui-nguyen-ban-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_bullitt_1968.jpg",
        "tam-tri-khong-sinh-ra-de-chong-lai-ban-no-chi-dang-boi-roi-trong-no-luc-bao-ve-ban-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dirty_harry.jpg",
        "su-xuat-sac-dich-thuc-khong-den-tu-viec-tu-vat-kiet-suc-luc-mot-cach-may-moc-no-la-nghe-thuat-dam-chim-vao-qua-trinh-duy-tri-mot-ngoi-nha.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_lethal_weapon.jpg",
        "hanh-trinh-tai-sinh-su-nu-tinh-thau-hieu-bong-toi-ban-nga-nghe-thuat-can-bang-cuc-tinh-science-long-form.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_point_break.jpg",
        "nexus-kien-truc-thong-tin-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_bad_boys_1995.jpg",
        "ky-luat-giao-tiep-giai-ma-tam-ly-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_mi_fallout.jpg",
        "giai-ma-vu-tru-thuyet-tu-gia-lap-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_casino_opening.jpg",
        "xa-hoi-da-lua-chung-ta-rang-hanh-phuc-la-mot-loai-cam-xuc-thuc-chat-cam-xuc-chi-la-tin-hieu-hanh-phuc-thuc-su-la-mot-ky-nang-va-su-lua-chon.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_good_will_hunting.jpg",
        "kichbanoffline-05-tiec-30-phut-lam-video-cho-ca-ngay.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_dead_poets_society.jpg",
        "how-to-get-rich-living-in-your-purpose-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_beautiful_mind.jpg",

        # 30 Movie Poster AI Covers
        "thu-gian-va-tieu-hoa-co-che.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_imitation_game.jpg",
        "top-sales-expert-simple-sales-trick-money-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_apollo_13.jpg",
        "suc-khoe-tinh-duc-tuoi-tho-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_first_man.jpg",
        "thien-kien-ca-nhan-hoa-sto.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_gravity_2013.jpg",
        "ban-hang-dinh-cao-tam-ly-hoc-chot-sale-shelby-sapp-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_the_martian.jpg",
        "giao-tiep-phi-ngon-ngu-khong-phai-la-de-thao-tung-no-la-he-thong-canh-bao-sinh-ton-duoc-khac-sau-vao-dna-cua-chung-ta-viec-thau-hieu-no-giup-ban-kien-tao-su-thoai-mai-tam-ly-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_sunshine_2007.jpg",
        "daniel-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_moon_2009.jpg",
        "ban-duoc-thiet-ke-de-song-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_oblivion_2013.jpg",
        "giai-ma-adn-than-thanh-mentor-learning.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_gyro_captain.jpg",
        "elon-musk-on-doge-tuong-lai-cua-ban-phu-thuoc-vao-nang-luc-cat-dut-dong-ro-ri-nang-luong-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_waterworld_1995.jpg",
        "level-up-your-communication-skills-masterclass-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_equilibrium_2002.jpg",
        "mo-hoa.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_book_of_eli.jpg",
        "ung-thu-khong-phai-la-mot-can-benh-di-truyen-ngau-nhien-no-la-can-benh-roi-loan-chuyen-hoa-bat-nguon-tu-viec-ty-the-nha-may-nang-luong-cua-te-bao-bi-ton-thuong-keo-dai-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_i_robot_2004.jpg",
        "thu-ban-nghi-minh-biet-ve-the-gioi-nay-chi-la-mot-mo-hinh-du-doan-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_chappie_2015.jpg",
        "khoa-hoc-cua-chap-tay-spiritual-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_district_9_mech.jpg",
        "su-thay-doi-thuc-su-khong-phai-la-co-gang-uon-nan-ban-than-thanh-mot-nguoi-hoan-toan-khac-no-la-qua-trinh-boc-tach-cac-lop-vo-boc-ao-tuong.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ready_player_one.jpg",
        "5-nghe-bien-mat.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_alita_battle_angel.jpg",
        "he-thong-ai-second-brain-va-tu-dong-hoa-vaibhav-sisinty-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_ghost_in_the_shell.jpg",
        "gioi-han-cua-y-chi-nguoi-quan-tuong-01.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_akira_1988.jpg",
        "nhan-ra-man-hinh-chieu-phim-cua-tam-thuc-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_princess_mononoke.jpg",
        "sunil-bajpai-fraud-scams-psychology-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_spirited_away.jpg",
        "sanjiv-goenka-wealth-turnaround-conglomerate-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_howls_moving_castle.jpg",
        "kichbanoffline-phau-thuat-kich-ban-6.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_castle_in_the_sky.jpg",
        "vi-sao-nguoi-khac-khong-thich-ban-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_nausicaa_valley.jpg",
        "shubhanshu-shukla-astronaut-space-zero-gravity-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/poster_neon_genesis_evangelion.jpg",

        # 30 Movie Poster AI Covers
        "bill-ackman-kich-ban-dau-tu.html": "./assets/covers/poster_256_mad_men.jpg",

        # 30 Movie Poster AI Covers
        "youtube-masterclass-highest-paid-strategist.html": "./assets/covers/poster_257_my_hero_academia.jpg",
        "boc-tran-cu-lua-diet-vong.html": "./assets/covers/poster_258_ice_age.jpg",
        "banner.html": "./assets/covers/poster_259_thien_menh_anh_hung.jpg",
        "banner-phan-tich-2-mau-poster-tatler-va-ket-qua-hinh-anh.html": "./assets/covers/poster_260_halt_and_catch_fire.jpg",
        "kichbanoffline-phau-thuat-kich-ban-5.html": "./assets/covers/poster_261_made_in_abyss.jpg",

        # 30 Movie Poster AI Covers
        "kichbanoffline-phau-thuat-kich-ban-4.html": "./assets/covers/poster_262_chicken_run.jpg",
        "kichbanoffline-phau-thuat-kich-ban-3.html": "./assets/covers/poster_263_that_son_tam_linh.jpg",
        "kichbanoffline-phau-thuat-kich-ban-2.html": "./assets/covers/poster_264_severance.jpg",
        "kichbanoffline-phau-thuat-kich-ban-1.html": "./assets/covers/poster_265_kill_la_kill.jpg",

        # 30 Movie Poster AI Covers
        "hanh-trinh-chua-lanh-nguyen-ban-podcast.html": "./assets/covers/poster_266_lion_king.jpg",
        "vi-du-ve-thue-bang-thong-va-giam-iq-science.html": "./assets/covers/poster_267_vi.jpg",
        "1000-ngay-sap-toi-gia-tri-lao-dong-tu-duy-cua-con-nguoi-mang-chi-so-am-podcast.html": "./assets/covers/poster_268_dexter.jpg",
        "new-way-to-win-as-content-creator-podcast.html": "./assets/covers/poster_269_death_parade.jpg",
        "make-first-100k-in-business-beginner-podcast.html": "./assets/covers/poster_271_quy_cau.jpg",

        # 30 Movie Poster AI Covers
        "so-tay-xay-kenh-thuat-toan-mentor-nguyen-duc-viet-podcast.html": "./assets/covers/poster_272_ozark.jpg",
        "mo-gawdat-giai-ma-hanh-phuc-ky-nguyen-ai-podcast.html": "./assets/covers/poster_273_fate_stay_night.jpg",
        "hau-het-met-moi-suong-mu-nao-lao-hoa-va-con-them-an-khong-phai-do-ban-thieu-y-chi-ma-do-tau-luon-sieu-toc-cua-glucose-trong-mau-khong-can.html": "./assets/covers/poster_274_kim_possible.jpg",
        "ky-luat-khac-ky-lam-chu-ban-than-giai-phong-tu-do-science-long-form.html": "./assets/covers/poster_275_chi_chi_em_em.jpg",
        "tu-duy-ai-tu-dong-hoa-science.html": "./assets/covers/poster_276_itaewon_class.jpg",

        # 30 Movie Poster AI Covers
        "giai-ma-noi-co-don-ty-do-brian-chesky-learning-experience-science-long-form.html": "./assets/covers/poster_281_1789612862471.jpg",
        "lauren-tan-kien-truc-agentic-1000-pr-dune-xai-cursor-podcast.html": "./assets/covers/poster_283_1789612886392.jpg",
        "tich-tru-ky-thuat-so-nguy-bien-suu-tam.html": "./assets/covers/poster_284_1789612900428.jpg",
        "blueprint-xay-kenh-jun-yuh-2026-podcast.html": "./assets/covers/poster_277_1789612731209.jpg",
        "lap-trinh-bo-nao-02-science.html": "./assets/covers/poster_279_1789612783772.jpg",
        "gat-bo-noi-so-bi-danh-gia-sao-chep-y-het-nhung-mo-hinh-dang-hoat-dong-tot-o-noi-khac-va-lien-tuc-kiem-chung-y-tuong-re-tien-thong-qua-internet-podcast.html": "./assets/covers/poster_280_1789612830358.jpg",

        # 30 Movie Poster AI Covers
        "so-tay-mentor-peak-span-giai-ma-sinh-hoc-podcast.html": "./assets/covers/poster_287_1789613082475.jpg",
        "complex-7-anxiety-is-not-what-you-think.html": "./assets/covers/poster_292_1789613142475.jpg",
        "performance-9-ai-is-starting-replacement-cycle.html": "./assets/covers/poster_286_1789613068457.jpg",
        "kien-tao-thuc-tai-learning-landing-page.html": "./assets/covers/poster_285_1789613054083.jpg",
        "ngon-ngu-co-the-khong-phai-vo-boc-no-la-ban-gioi-thieu-cua-tam-tri-science-long-form.html": "./assets/covers/poster_291_1789613131027.jpg",
        "tamlyhoc.html": "./assets/covers/poster_282_1789613041805.jpg",
        "the-new-way-to-make-money-online-podcast.html": "./assets/covers/poster_288_1789613094818.jpg",

        # 30 Movie Poster AI Covers
        "giac-ngu-ngan-20-phut-science.html": "./assets/covers/poster_298_1789613337071.jpg",
        "ky-nguyen-ai-va-bien-dong-tot-do-science.html": "./assets/covers/poster_295_1789613299042.jpg",
        "10-thien-kien-tien-hoa-science.html": "./assets/covers/poster_296_1789613313929.jpg",
        "gioi-han-cua-y-chi-nguoi-quan-tuong-02-spiritual-sto.html": "./assets/covers/poster_300_1789613362843.jpg",
        "family-time-entrepreneur-wake-up-call-podcast.html": "./assets/covers/poster_289_1789613108788.jpg",
        "truc-giac-la-he-thong-phong-thu-sinh-ton-toi-thuong-vuot-troi-hon-logic-science.html": "./assets/covers/poster_293_1789613273938.jpg",
        "sovereignty-vitality-masterclass-podcast.html": "./assets/covers/poster_297_1789613323067.jpg",
        "law-8-were-massively-underestimating-ai.html": "./assets/covers/poster_290_1789613262649.jpg",
        "ai-co-y-thuc-stuart_russell-science.html": "./assets/covers/poster_294_1789613286524.jpg",
        "giai-ma-tien-loi-chet-nguoi-learning-landing-page-podcast.html": "./assets/covers/poster_278_1789613248069.jpg",
        "de-che-tam-tri-cua-simon-cowell-science.html": "./assets/covers/poster_299_1789613349759.jpg",

        # 30 Movie Poster AI Covers
        "nam-cot-loi-don-dau-chu-ky-hack-ban-nga-ray-dalio-science.html": "./assets/covers/poster_331_bay_rong.jpg",
        "giai-ma-giao-tiep-giai-tru-thao-tung-science.html": "./assets/covers/poster_332_arcane.jpg",
        "ban-sinh-ra-khong-phai-de-thuan-theo-conform-cai-khuon-duc-san-cua-xa-hoi-ma-de-chuyen-hoa-podcast.html": "./assets/covers/poster_333_no_game.jpg",
        "giai-ma-hanh-vi-loi-ich-vo-ly-01-science.html": "./assets/covers/poster_334_sing.jpg",
        "simon-sinek-trust-crisis-gen-z-burnout-leadership-podcast.html": "./assets/covers/poster_335_bi_dung_so.jpg",
        "de-che-mrbeast-podcast.html": "./assets/covers/poster_336_fallout.jpg",
        "kiran-mazumdar-shaw-biotech-founder-india-podcast.html": "./assets/covers/poster_337_hunter_x_hunter.jpg",
        "how-to-charge-more-for-knowledge-value-pricing-podcast.html": "./assets/covers/poster_338_shrek.jpg",
        "so-tay-rucking-thuc-chien-science-long-form.html": "./assets/covers/poster_339_qua_tim_mau.jpg",
        "ban-khong-chon-ban-doi-chi-de-chup-nhung-tam-anh-dep-vao-ngay-cuoi-podcast.html": "./assets/covers/poster_340_witcher.jpg",
        "y-hoc-30-chu-dong-can-thiep-tu-som-coi-tap-luyen-la-loai-thuoc-manh-nhat-va-muc-tieu-la-keo-dai-tuoi-tho-khoe-manh-healthspan-thay-vi-chi.html": "./assets/covers/poster_341_rezero.jpg",
        "sinh-vat-sinh-hoc-bi-chi-phoi-manh-me-boi-khao-khat-sinh-ton-va-duy-tri-noi-giong-khoa-hoc-khong-dung-de-bien-minh-cho-toi-loi-ma-de-cap-cho-ta-tam-ban-do-dieu-huong-nhung-phan-con-ben-trong-minh-podcast-science.html": "./assets/covers/poster_342_powerpuff.jpg",
        "khoi-nghiep-ky-nguyen-moi-science.html": "./assets/covers/poster_343_trang_quynh.jpg",
        "hay-ngung-dua-vao-y-chi-hay-cam-tinh-de-ra-quyet-dinh-song-bang-cach-thiet-lap-thuat-toan-ky-luat-blueprint-va-de-du-lieu-len-tieng-ban-co.html": "./assets/covers/poster_344_money_heist.jpg",
        "system-7-the-3-ways-pressure-breaks-you.html": "./assets/covers/poster_345_psycho_pass.jpg",
        "ban-co-the-an-kieng-hoan-hao-tap-gym-moi-ngay-ngu-du-8-tieng-nhung-neu-ban-hit-tho-sai-cach-ban-van-se-luon-luon-om-yeu-99-nhan-loai-dang.html": "./assets/covers/poster_346_monsters_inc.jpg",
        "tam-ly-follow-instagram-vo-thuc.html": "./assets/covers/poster_347_ao_lua_ha_dong.jpg",
        "duong-ruot-gut-va-tam-tri-feelings-la-hai-mat-cua-cung-mot-dong-xu-de-chua-lanh-su-kiet-que-va-benh-tat-ban-khong-the-chi-uong-thuoc-ban.html": "./assets/covers/poster_348_peaky_blinders.jpg",
        "complex-9-happiness-is-a-choice.html": "./assets/covers/poster_349_kengan_ashura.jpg",
        "lam-chu-tam-tri-dung-de-nao-bo-huy-hoai-cuoc-doi-ban-podcast-dan-kief.html": "./assets/covers/poster_350_turning_red.jpg",
        "giai-ma-trang-thai-flow-song-cuoc-doi-troi-chay-podcast.html": "./assets/covers/poster_351_co_hau_gai.jpg",
        "tinh-yeu-ben-vung-khong-phai-la-dinh-menh-may-rui-hay-tia-lua-tinh-yeu-bung-chay-trong-lan-gap-dau-tien-no-la-ket-qua-cua-mot-chuoi-nhung.html": "./assets/covers/poster_352_silicon_valley.jpg",
        "du-doan-va-quan-ly-ngan-sach-nang-luong-cua-co-the-science.html": "./assets/covers/poster_353_chainsaw_man.jpg",
        "khoa-hoc-nao-bo-10x-tap-trung-va-tri-nho-dr-sahar-yousef-podcast.html": "./assets/covers/poster_354_cars.jpg",
        "giai-ma-hoi-rosicrucian-kien-truc-hoa-nang-luong-thuc-tinh-tam-linh.html": "./assets/covers/poster_355_tam_cam.jpg",
    }

    for f in files:
        if f in exclude:
            continue
            
        filepath = os.path.join(os.getcwd(), f)
        stat = os.stat(filepath)
        mod_time = datetime.fromtimestamp(stat.st_mtime).isoformat()
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else f.replace('.html', '').replace('-', ' ').title()
            
            # Simple excerpt (first paragraph with text > 50 chars)
            excerpt = "Bài viết chuyên sâu từ kho dữ liệu Antigravity."
            for p in soup.find_all('p'):
                text = p.text.strip()
                if len(text) > 50:
                    excerpt = text[:150] + "..."
                    break
                    
            # Determine category based on filename keywords
            fname_lower = f.lower()
            if 'broll' in fname_lower or 'quay' in fname_lower:
                cat = "broll"
                cat_label = "🎬 B-Roll & Cảnh Trám"
            elif 'podcast' in fname_lower:
                cat = "science"
                cat_label = "🧠 Tâm Lý & Não Bộ"
            elif 'science' in fname_lower:
                cat = "science"
                cat_label = "🧠 Khoa Học"
            else:
                cat = "other"
                cat_label = "📌 Bài Viết"
                
        cover_img = cover_mapping.get(f, "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80")

        posts.append({
            "filename": f,
            "title": title,
            "excerpt": excerpt,
            "category_key": cat,
            "category_label": cat_label,
            "cover_image": cover_img,
            "updated_at": mod_time,
            "read_time": "5 phút đọc",
            "file_size_kb": round(stat.st_size / 1024)
        })

    # Sort by updated_at descending
    posts.sort(key=lambda x: x['updated_at'], reverse=True)

    with open('posts-manifest.json', 'w', encoding='utf-8') as out:
        json.dump({"posts": posts}, out, ensure_ascii=False, indent=2)
        
    print(f"Generated manifest with {len(posts)} posts.")

if __name__ == "__main__":
    generate()
