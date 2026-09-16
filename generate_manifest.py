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
