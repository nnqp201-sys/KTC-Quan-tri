# Mô tả chi tiết Hệ thống KTC trên Claude (Chat – Cowork – Code)
## Kèm mô tả Plugin / Skill / Agent tự phát triển trong tài khoản — phục vụ nâng cấp hệ thống

**Ngày lập:** 2026-09-01
**Tài khoản:** phongthhcqt@gmail.com
**Nguồn tổng hợp:**
1. `Bao-Cao-Mo-Ta-He-Thong-hệ thống KTC-1_1 (2).docx` (lập 26/8/2026, lưu hành nội bộ Phòng TH-HC&QT) — sau đây gọi là **"Báo cáo gốc"**.
2. Trạng thái thực tế tài khoản tại thời điểm lập tài liệu này: `ListSkills`, `ListAgents`, và kho nguồn `KTC-Ra-Soat-897-Universal-Plugin` (Google Drive, thư mục làm việc hiện tại).

> Tài liệu này **không thay thế** Báo cáo gốc mà mở rộng nó theo hai hướng: (a) làm rõ khác biệt vận hành giữa ba nền tảng Claude Chat / Cowork / Claude Code, và (b) đối chiếu mô tả trong Báo cáo gốc với những gì thực sự đang tồn tại trong tài khoản, để lộ ra các khoảng lệch cần xử lý trước khi nâng cấp.

---

## I. Tổng quan hệ sinh thái hệ thống KTC

hệ thống KTC (KTC Digital Intelligence System) là tập hợp **5 hệ AI độc lập**, vận hành trên nền Google Drive + Claude, phục vụ công tác hành chính/kế hoạch/báo cáo/quản lý dữ liệu của Trường Cao đẳng Kon Tum. Mỗi hệ đóng gói dưới dạng Skill riêng, có thể cài/dùng độc lập.

| STT | Tên hệ | Chức năng chính |
|---|---|---|
| 1 | KTC-Ra-Soat-897-v2-Cai-tien | Rà soát, so sánh, chuẩn hóa văn bản trước khi trình ký |
| 2 | KTC-DIS-Tong-Hop-VB | Soạn thảo, rà soát, chuẩn hóa văn bản hành chính (đầy đủ nhất — 30 skill con) |
| 3 | KTC-Ke-Hoach (KTC-PIS) | Xây dựng kế hoạch công tác năm/quý/tháng theo 6 Trục kết quả |
| 4 | KTC-Bao-Cao (KTC-RIS) | Tổng hợp báo cáo công tác từ các đơn vị theo 6 Trục và KPI 3 chiều |
| 5 | KTC-Database | Quản lý kho dữ liệu nền dùng chung 01–04 (văn bản pháp lý, quy định, mẫu, tài liệu tốt) |

**Nguyên tắc kiến trúc cốt lõi (Báo cáo gốc, Phần I):** 5 hệ **không** dùng chung một kho trung tâm theo nghĩa đen — mỗi hệ giữ **bản sao riêng** của tài liệu nguyên tắc chung (`00-Nguyen-Tac-Chung.md`) và `Skill-Library` riêng. Đồng bộ nội dung dùng chung (ví dụ quy tắc viện dẫn văn bản hợp nhất) phải **nhân bản thủ công vào cả 5 vị trí** — không có cơ chế lan tỏa tự động.

**Quan hệ giữa các hệ (Báo cáo gốc, Phần IV):**

| Từ hệ | Đến hệ | Mối quan hệ |
|---|---|---|
| KTC-Ke-Hoach | KTC-Ra-Soat-897 | Gọi rà soát chính thức trước khi trình ký kế hoạch |
| KTC-Bao-Cao | KTC-Ra-Soat-897 | Gọi rà soát chính thức trước khi trình ký báo cáo |
| KTC-Ra-Soat-897 | KTC-Bao-Cao | Học chuẩn phong cách báo cáo qua Skill-Tu-hoc |
| KTC-Ra-Soat-897 | KTC-Database | Đối chiếu kho 01–04 trước mọi lần rà soát (Nguyên tắc 1) |
| KTC-DIS-Tong-Hop-VB | KTC-Database | Tham chiếu văn bản pháp lý gốc, mẫu chuẩn khi soạn thảo |
| Tất cả 5 hệ | Tất cả 5 hệ | Dùng chung Skill Track Changes, Skill giải trình (đặt tại KTC-Database, nhân bản khi cần) |

Luồng quan hệ hiện tại chủ yếu là **"gọi đơn hướng"**: các hệ soạn thảo/kế hoạch/báo cáo gọi KTC-Ra-Soat-897 để rà soát, nhưng KTC-Ra-Soat-897/KTC-Database **chưa** có cơ chế chủ động đẩy cập nhật quy tắc chung ngược lại các hệ kia.

---

## II. Bốn hệ quy chiếu pháp lý (Bước 0 — nền tảng của mọi tác vụ rà soát/soạn thảo)

| Hệ | Loại văn bản | Căn cứ áp dụng |
|---|---|---|
| A | Hành chính nhà nước | NĐ 30/2020/NĐ-CP + TB 597/TB-CĐKT (quy ước riêng Trường) |
| B | Văn bản của Đảng | HD 05-HD/VPTW (27/5/2026) — **tuyệt đối không áp NĐ 30** |
| C | Văn bản quy phạm pháp luật | Luật Ban hành VBQPPL |
| D | Văn bản đoàn thể | 3 tiểu-hệ: Công đoàn (có Quốc hiệu) · Đoàn Thanh niên (tiêu đề riêng + 3 sao) · Hội Sinh viên (không dòng tiêu đề) |

Phân loại mức độ vấn đề (áp dụng thống nhất mọi hệ có chức năng rà soát):

| Mức | Ý nghĩa | Ví dụ |
|---|---|---|
| 1 | Bắt buộc sửa — ảnh hưởng hiệu lực pháp lý | Viện dẫn văn bản hết hiệu lực, sai thẩm quyền |
| 2 | Cần sửa — ảnh hưởng chất lượng, thể thức | Sai ký hiệu KT./K/T., thiếu số 0 trong ngày tháng |
| 3 | Nên sửa — quy ước riêng của Trường | Viết hoa sau dấu ":", dùng sai chữ "bảo đảm" |
| 4 | Góp ý nâng cao — không bắt buộc | Văn phong, cách trình bày có thể cải thiện |

---

## III. Kiến trúc triển khai trên 3 nền tảng Claude

Đây là phần mở rộng so với Báo cáo gốc (Báo cáo gốc mô tả hệ ở mức nghiệp vụ, chưa tách rõ theo runtime). Theo `CORE-INDEX.md` của Universal Plugin, quy tắc runtime hiện hành là:

| Nền tảng | Công cụ khả dụng | Đặc điểm vận hành |
|---|---|---|
| **Claude Chat** | Chỉ Skills | Không có binary/tool thực thi thật (không đọc được byte nhị phân file .docx) → **mọi kiểm tra định lượng (lề, cỡ chữ) phải ghi rõ "chưa xác minh"** (`FORMAT_BINARY_UNVERIFIED`) thay vì suy đoán từ nội dung text hiển thị. |
| **Cowork** | Skills + Subagents + Connectors + Local file tools (khi được cấp quyền) | Có thể đọc file thật qua connector (Drive, v.v.), triển khai được cơ chế multi-agent (rà soát pháp lý/logic/thể thức/bằng chứng song song), nhưng phụ thuộc quyền connector được cấp trong phiên. |
| **Claude Code** | Skills + Subagents + Hooks + Bin scripts | Nền tảng **duy nhất** chạy được script quyết định (python-docx đọc `section.*_margin`, `run.font.size` thật), có `SessionStart` hook tự kiểm tra môi trường (`ktc897-doctor`) và `PreToolUse` hook chặn thao tác phá hoại (`guard_destructive.py`). Đây là nơi "strict plugin validation" (`claude plugin validate --strict`) chạy trước khi release. |

**Hệ quả trực tiếp cho chất lượng đầu ra:** cùng một yêu cầu rà soát thể thức sẽ cho kết quả tin cậy khác nhau tùy nền tảng — Claude Code là nơi duy nhất đo được lề/cỡ chữ *thật* trên byte nhị phân (cơ chế từ v2.15, xem mục IV.6.1); Chat và Cowork (khi không có tool đọc byte) phải trung thực ghi nhận giới hạn này thay vì kết luận sai.

---

## IV. Hệ KTC-Ra-Soat-897 — mô tả chi tiết theo 2 nhánh song song

Đây là hệ được kiểm thử sâu nhất trong hệ thống KTC. **Tài khoản hiện có đồng thời 2 nhánh phát triển của cùng một hệ nghiệp vụ**, cần phân biệt rõ khi nâng cấp:

### IV.A. Nhánh Skill độc lập (Chat/Cowork) — theo Báo cáo gốc, phiên bản v2.17

- **Mục đích:** rà soát dự thảo trước khi trình ký theo TB 897/TB-CĐKT (04/8/2026). 4 tác vụ: rà soát chính thức · rà soát nhanh · so sánh 2 phiên bản · chuẩn hóa văn phong. **Không soạn thảo mới.**
- **Kết cấu báo cáo rà soát chính thức — 8 phần chuẩn:** I. Thông tin chung → II. Kết quả rà soát chi tiết → III. Nội dung đạt → IV. Bảng tổng hợp → V. Thẩm định chuyên môn (bắt buộc có điều kiện) → VI. Đánh giá tổng thể → VII. Kết luận và thứ tự xử lý → VIII. Phân tích khả thi và rủi ro (tùy chọn). Định dạng: A4 ngang 297×210mm, lề 20mm đều 4 phía, Times New Roman 14pt.
- **Cơ chế kỹ thuật đã tích hợp:**
  - *v2.15* — đọc thuộc tính định dạng thật (`29-Cong-Cu/_read_input_properties.py`, python-docx: `section.*_margin`, `run.font.size`/`bold`) thay vì chỉ đọc `paragraph.text` → khắc phục việc mọi lỗi định lượng (lề sai, cỡ chữ sai) từng bị bỏ sót.
  - *v2.17* — vá lỗi làm tròn ngưỡng biên: sai số dấu phẩy động khi quy đổi Cm/Mm (20.0mm → 20.0025mm) từng gây báo sai; vá bằng `round(val,1)` + `EPS=0.01`, kiểm thử bằng 3 test case.
  - *v2.16* — Skill viện dẫn văn bản hợp nhất: mã hóa Điều 4 Pháp lệnh Hợp nhất VBQPPL số 01/2012/UBTVQH13 (sửa đổi bởi PL 01/2026/UBTVQH16); nhân bản vào cả 5 Hệ thống KTC; trigger tự động khi gặp "hợp nhất"/"VBHN".
  - *26/8/2026* — Cơ chế tự kích hoạt (`00c-Co-Che-Tu-Kich-Hoat.md`): gộp 4 bước bắt buộc (đọc bộ nhớ vận hành, quét cụm từ kích hoạt, chạy Bước 0 + script định lượng, kích hoạt Skill tự học báo cáo) thành 1 quy trình chạy ngay khi nạp Skill, không phụ thuộc người dùng nhắc lại. Ra đời sau 2 lần ghi nhận lệch số phiên bản giữa tài liệu điều khiển.
- **Kết quả kiểm thử hồi quy** (bộ `File-Test-Loi-KTC897.docx`, 30 lỗi cài sẵn):

  | Phiên bản | Đúng hoàn toàn | Sai mức | Bỏ sót | Ghi chú |
  |---|---|---|---|---|
  | v2.14 | 8/28 (28,6%) | 7/28 (25%) | 13/28 (46,4%) | Baseline |
  | v2.16 | 8/28 (28,6%) | 7/28 (25%) | 13/28 (46,4%) | Chưa đo được thuộc tính định lượng |
  | v2.17 | 12/30 (40%) | 7/30 (23,3%) | 11/30 (36,7%) | Đo THẬT trên file gốc — tăng 11,4 điểm % |

- **Cấu trúc thư mục:** `00-README.md`, `SKILL.md`, `ktc-ra-soat-897-v2.17.skill` · `assets/` · `references/` (Checklist 01–08, Skill-Library, Prompt-Library) · `29-Cong-Cu/` (`build_ktc897_report.py` v3.0, `_read_input_properties.py`) · `30-Ket-Qua/` (nguồn tự học) · `13-Regression-Test/` · `09-Quan-Tri-He/10-Bo-Nho-He/`.

### IV.B. Nhánh Universal Plugin (Claude Chat + Cowork + Claude Code) — kho nguồn đang phát triển tại đây

Đây là hướng đi **chưa có** trong Báo cáo gốc (26/8/2026) — được khởi tạo cùng ngày báo cáo gốc được lập, hiện là nhánh **DEVELOPMENT/ALPHA**, mục tiêu thống nhất 1 core nghiệp vụ chạy trên cả 3 nền tảng thay vì 1 Skill rời cho Chat/Cowork.

**Trạng thái song song (Parallel Run Policy):**

| Nhánh | Trạng thái |
|---|---|
| `KTC-Ra-Soat-897-v2-Cai-tien` | PRODUCTION / STABLE / read-only từ Universal |
| `KTC-Ra-soat-897-v3.0` | RELEASE CANDIDATE / SHADOW / read-only từ Universal |
| `KTC-Ra-Soat-897-Universal-Plugin` | DEVELOPMENT / ALPHA |

Quy tắc: cùng một hồ sơ thử nghiệm phải chạy độc lập trên cả 3 nhánh; Universal **không được đọc** output của v2/v3 trước khi hoàn thành blind run; chỉ chuyển Production khi GO gate được phê duyệt.

**Nguồn sự thật duy nhất (`SOURCE-OF-TRUTH.md`):** `core/` ở cấp repo là nguồn nghiệp vụ duy nhất; `plugin/core/` là **snapshot sinh ra** bởi `29-Cong-Cu/build_universal.py`; `dist/` là artifact sinh ra, không sửa tay; v2.x/v3.0 chỉ để so sánh/rollback, không bị build Universal ghi đè.

**Cấu trúc plugin đã đóng gói (`dist/ktc-ra-soat-897-universal-0.1.0-alpha.1.zip`, 87 file):**

```
.claude-plugin/plugin.json        — manifest chính (defaultEnabled: false)
agents/                           — 4 subagent chuyên biệt (xem mục V)
bin/                              — ktc897-build, ktc897-doctor, ktc897-properties
core/                             — snapshot Core v3.0-RC (rules, checklist 01–09, Prompt-Library,
                                     Skill-Library, templates .docx/.dotx, schemas, tools python)
hooks/hooks.json                  — SessionStart + PreToolUse guard
scripts/guard_destructive.py      — chặn thao tác phá hoại trước Bash/PowerShell/Write/Edit
skills/                           — 4 skill cổng vào: review, quick-review, compare, normalize
```

**Versioning & Release Gates (`RELEASE-POLICY.md`):** SemVer độc lập với số phiên bản nghiệp vụ KTC-Ra-Soat-897 (MAJOR = breaking runtime/plugin contract, MINOR = capability mới, PATCH = fix, pre-release `alpha.N/beta.N/rc.N`). Điều kiện lên phiên bản: Claude strict validation PASS · deterministic/unit tests PASS · regression/negative controls PASS theo ngưỡng phê duyệt · không có blocker Mức 1 mới so với v2.x · rollback artifact còn sẵn.

---

## V. Mô tả chi tiết Plugin / Skill / Agent tự phát triển trong tài khoản (xác nhận thực tế)

### V.1. Plugin

`ListPlugins` (cấp claude.ai) trả về **rỗng** — chưa có plugin nào ở trạng thái account-level "đã cài/bật" qua marketplace. Plugin `ktc-ra-soat-897` (Universal) mô tả ở mục IV.B hiện chỉ tồn tại dưới dạng **source cục bộ** trong repo này; chưa có `.claude-plugin/marketplace.json` ở gốc repo nên chưa dùng được `claude plugin marketplace add` (cục bộ hay GitHub `phongthhcqt-commits/ktc-ra-soat-897-plugin`) — lệnh `/plugin` không khả dụng trong môi trường phiên hiện tại để kiểm chứng trực tiếp.

### V.2. Skills tự phát triển đang bật trên tài khoản

| Skill | Vai trò | Ghi chú đối chiếu |
|---|---|---|
| `ktc-ra-soat-897` | Rà soát/so sánh/chuẩn hóa theo TB 897 (4 hệ quy chiếu A/B/C/D + quy ước TB 597) | Tương ứng nhánh IV.A |
| `ktc-ra-soat-897-universal-0-1-0-alpha-5` | Bản Universal alpha, dùng chung Chat/Cowork/Code | **Alpha.5** — mới hơn bản `0.1.0-alpha.1` đang mirror trong repo Drive này (xem khoảng lệch ở mục VI) |
| `ktc-bao-cao` | Tổng hợp báo cáo công tác từ Excel TB736 theo 6 Trục + KPI 3 chiều | = Hệ #4 KTC-Bao-Cao (KTC-RIS) trong Báo cáo gốc |
| `ktc-ke-hoach` | Tổng hợp kế hoạch công tác năm/quý/tháng theo 6 Trục | = Hệ #3 KTC-Ke-Hoach (KTC-PIS) trong Báo cáo gốc |
| `ktc-database` | Quản lý kho dữ liệu nền 01–04 (Legal-Database, Regulations, Templates, Good-Documents) | = Hệ #5 KTC-Database trong Báo cáo gốc |

Bên trong nhánh Universal Plugin (IV.B), 4 skill cổng vào (`skills/*/SKILL.md`) chia nhỏ đúng 4 tác vụ nghiệp vụ:

| Skill con | Chức năng | Ràng buộc quan trọng |
|---|---|---|
| `review` | Rà soát chính thức | Bắt buộc nạp `CORE-INDEX.md` + `00-RUNTIME-INVARIANTS.md` + Core v3.0 trước khi kết luận; chạy `ktc897-properties` nếu runtime cho phép, nếu không → ghi `FORMAT_BINARY_UNVERIFIED`; xuất báo cáo bằng `ktc897-build` và ghi Process Memory khi runtime cho phép |
| `quick-review` | Rà soát nhanh/sơ bộ | Vẫn bắt buộc xác định hệ A/B/C/D trước; không tự nâng thành rà soát chính thức nếu người dùng không yêu cầu |
| `compare` | So sánh 2 phiên bản | Phân loại: đã tiếp thu / tiếp thu một phần / chưa tiếp thu / phát sinh mới; không tin nhãn "đã sửa" nếu nội dung không khớp |
| `normalize` | Chuẩn hóa văn phong | Chỉ chuẩn hóa văn bản có sẵn, không mở rộng thành soạn mới; nếu sửa DOCX trực tiếp phải giữ Track Changes |

*(Skill có sẵn của Anthropic dùng kèm, không phải tự phát triển: `docx`, `xlsx`, `pptx`, `pdf`, `morning`, `import-memory`, `skill-creator`.)*

### V.3. Agents tự phát triển (subagent, thuộc plugin `ktc-ra-soat-897`)

| Agent | Vai trò | Ràng buộc kỹ thuật (từ định nghĩa thật trong plugin) |
|---|---|---|
| `legal-reviewer` | Rà soát căn cứ, hiệu lực, thẩm quyền, rủi ro pháp lý | `disallowedTools: Write, Edit`, `maxTurns: 12`. Chỉ kết luận khi nguồn đủ mạnh; ≥2 khả năng hợp lý hoặc thiếu nguồn → trả `CẦN XÁC MINH`. Không sửa file nguồn, không tự gán trạng thái phê duyệt. |
| `logic-reviewer` | Kiểm tra logic, tính thống nhất, thuật ngữ, số liệu, mâu thuẫn nội dung | `disallowedTools: Write, Edit`, `maxTurns: 10`. Không tin nhãn "đã sửa"; tách lỗi logic khỏi lỗi pháp lý/thể thức; tính lại độc lập số liệu/định mức khi đủ dữ liệu. |
| `format-reviewer` | Kiểm tra thể thức, số ký hiệu, tên cơ quan, lề, cỡ chữ | `disallowedTools: Write, Edit`, `maxTurns: 10`. Bắt đầu bằng phân hệ A/B/C/D; không áp NĐ 30 sang Đảng/Đoàn thể; chỉ đánh giá lề/cỡ chữ từ measurement thật do tool cung cấp, ngược lại ghi chưa xác minh; ưu tiên Checklist 08 (quy ước riêng Trường) trước quy tắc chung. |
| `evidence-verifier` | Xác minh bằng chứng/nguồn cho finding trọng yếu — lớp kiểm tra chéo cuối | `disallowedTools: Write, Edit`, `maxTurns: 8`. Với mọi finding Mức 1 hoặc kết luận chặn trình ký: kiểm nguồn, vị trí, hiệu lực thời gian, quan hệ sửa đổi/thay thế; không đủ bằng chứng → hạ xuống `CẦN XÁC MINH`, không tự bổ sung dữ kiện. |
| `ktc-eval` | Chấm blind regression độc lập theo Golden Dataset (Chat/Cowork/Code) | Không dùng để tự phê duyệt production. *(Hiện diện trong danh sách agent khả dụng của tài khoản nhưng không thấy trong gói `dist/…alpha.1.zip` đang mirror ở Drive — khả năng thuộc bản `alpha.5` mới hơn, xem mục VI.)* |

Cả 4 agent trong gói alpha.1 đều **không có quyền Write/Edit** — thiết kế đúng nguyên tắc "lớp kiểm tra chéo chỉ đọc, không tự sửa", tránh một agent vừa phát hiện lỗi vừa tự ý sửa mà không qua kiểm chứng.

### V.4. Công cụ tất định (bin/scripts) — nền tảng của độ tin cậy đo lường

| Script | Chức năng |
|---|---|
| `bin/ktc897-doctor` | Chạy trong `SessionStart` hook — tự kiểm tra môi trường plugin khi phiên Claude Code khởi động |
| `bin/ktc897-properties` | Wrapper gọi `_read_input_properties.py` — đọc lề/cỡ chữ thật từ file .docx |
| `bin/ktc897-build` | Wrapper gọi `build_ktc897_report.py` — xuất báo cáo rà soát 8 phần chuẩn |
| `core/tools/_read_input_properties.py` | Đọc `section.*_margin`, `run.font.size/bold` bằng python-docx (cơ chế v2.15) |
| `core/tools/build_ktc897_report.py` (v3.0) | Sinh báo cáo .docx theo schema `core/schemas/review-output.schema.json` |
| `core/tools/validate_v3.py`, `test_margin_boundary.py`, `test_multisection_properties.py`, `test_report_layout_v3.py` | Bộ kiểm thử tất định — nền của "Regression/negative controls PASS" trong Release Gates |
| `scripts/guard_destructive.py` | Chạy trong `PreToolUse` hook, matcher `Bash\|PowerShell\|Write\|Edit` — chặn/cảnh báo thao tác phá hoại trước khi thực thi |

---

## VI. Đối chiếu Báo cáo gốc vs Trạng thái thực tế tài khoản — khoảng lệch cần xử lý trước khi nâng cấp

| # | Phát hiện | Chi tiết | Rủi ro nếu bỏ qua |
|---|---|---|---|
| 1 | **Lệch phiên bản Universal Plugin** | Tài khoản đang bật `ktc-ra-soat-897-universal-0-1-0-alpha-5`, nhưng kho nguồn Drive (`KTC-Ra-Soat-897-Universal-Plugin/`) chỉ có snapshot đóng gói tới `0.1.0-alpha.1` (`plugin.json`, `dist/…alpha.1.zip`, `CHANGELOG.md` dừng ở alpha.1) | Không thể xác minh alpha.2→alpha.5 đã thay đổi gì so với source hiện có trên Drive → vi phạm chính nguyên tắc "Single Source of Truth" mà repo này đặt ra cho chính nó |
| 2 | **`ktc-eval` không có trong gói alpha.1** | Agent `ktc-eval` xuất hiện trong danh sách agent khả dụng của tài khoản (mô tả: chấm blind regression theo Golden Dataset) nhưng không có file `agents/ktc-eval.md` trong `dist/…alpha.1.zip` | Không rõ agent này được định nghĩa version nào, ràng buộc tool gì — cần đối chiếu với bản alpha.5 trước khi coi là đã kiểm thử |
| 3 | **`KTC-DIS-Tong-Hop-VB` vắng mặt trong Skill đang bật** | Báo cáo gốc mô tả đây là hệ soạn thảo đầy đủ nhất (30 skill con), nhưng `ListSkills` của tài khoản hiện tại **không** liệt kê skill này | Cần xác minh: (a) chưa cài trên tài khoản này, (b) tên định danh khác, hay (c) chỉ tồn tại như tài liệu Drive chưa đóng gói thành Skill claude.ai |
| 4 | **Cơ chế đồng bộ vẫn thủ công, mới tự động hóa được 1/5 hệ** | Universal Plugin đã có `29-Cong-Cu/build_universal.py` + `SOURCE-OF-TRUTH.md` để tự động sinh `plugin/core/` từ `core/` — đúng hướng khuyến nghị #3 của Báo cáo gốc ("xây dựng cơ chế đồng bộ tự động") — nhưng phạm vi mới áp dụng cho riêng KTC-Ra-Soat-897, 4 hệ còn lại (Tong-Hop-VB, Ke-Hoach, Bao-Cao, Database) chưa có cơ chế tương đương | Nếu nâng cấp tiếp tục theo hướng Universal Plugin, cần quyết định sớm: nhân rộng mô hình `core/` + build script này cho cả 5 hệ, hay giữ 4 hệ kia ở mô hình Skill rời như hiện tại |
| 5 | **Thư mục `agents/`, `bin/`, `scripts/` trên Drive chỉ có `desktop.ini`** | Đúng như `plugin/DIRECT-MIRROR-STATUS.md` đã cảnh báo: nội dung thật (agent .md, bin script) chỉ tồn tại trong `dist/…zip`, chưa materialize dạng file rời trên cây Drive mirror | Người thao tác trực tiếp trên cây `31-Plugin/` qua Drive UI (không giải nén zip) sẽ **không thấy** agent/script thật — dễ tưởng nhầm là thiếu, hoặc sửa nhầm bản không phải nguồn |
| 6 | **`.claude-plugin/marketplace.json` chưa tồn tại** | Đã xác nhận ở phiên làm việc trước — cần quyết định nguồn trỏ (`./plugin` hay file zip `dist/`) trước khi tạo, mới dùng được `/plugin marketplace add` | Không tạo được marketplace cục bộ/GitHub cho tới khi hoàn tất |

---

## VII. Khuyến nghị nâng cấp (kế thừa Báo cáo gốc, Phần VI.2 + bổ sung mới)

**Từ Báo cáo gốc:**
1. Hoàn thiện Skill/Checklist riêng cho hệ quy chiếu D — đoàn thể (Công đoàn, Đoàn TN, Hội SV) — khoảng trống lớn nhất, tỷ lệ phát hiện đúng thấp nhất trong 4 hệ quy chiếu.
2. Cập nhật `SKILL.md` của 4 hệ còn lại để dẫn chiếu tường minh tới cơ chế trigger dùng chung (hiện chỉ có file vật lý, chưa có dòng gọi trong `SKILL.md`).
3. Xem xét cơ chế đồng bộ tự động thay thế nhân bản thủ công giữa 5 hệ nếu tần suất cập nhật tăng.
4. Bổ sung đầy đủ hồ sơ Process Memory cho các ca rà soát chính thức đã thực hiện.

**Bổ sung mới từ đối chiếu ở Mục VI (ưu tiên trước khi nâng cấp tiếp Universal Plugin):**
5. Đồng bộ ngay kho nguồn Drive với phiên bản `alpha.5` đang chạy thật trên tài khoản — tránh tình trạng "Single Source of Truth" bị chính nó vi phạm.
6. Xác minh và tài liệu hóa agent `ktc-eval` (định nghĩa, `disallowedTools`, `maxTurns`) trước khi dùng làm căn cứ chấm regression cho quyết định go/no-go.
7. Làm rõ trạng thái `KTC-DIS-Tong-Hop-VB` trên tài khoản này — cài lại nếu cần, hoặc ghi nhận rõ đây là hệ chỉ dùng ở tài khoản/nơi làm việc khác.
8. Quyết định phạm vi áp dụng mô hình `core/` tập trung + build script: mở rộng cho cả 5 Hệ thống KTC, hay giữ nguyên hiện trạng (chỉ Ra-Soat-897) và chấp nhận 4 hệ kia tiếp tục đồng bộ thủ công.
9. Tạo `.claude-plugin/marketplace.json` ở gốc repo (đã nêu ở phiên trước) để có đường cài đặt chính thức, thay vì phụ thuộc thao tác thủ công trên Drive dễ nhầm bản (xem Mục VI, dòng 5).

---

*Tài liệu tổng hợp phục vụ nội bộ, dùng làm đầu vào cho việc lập kế hoạch nâng cấp hệ thống KTC trong thời gian tới. Phần mô tả nghiệp vụ 5 hệ kế thừa nguyên trạng từ Báo cáo gốc (26/8/2026); phần đối chiếu Mục VI và khuyến nghị bổ sung Mục VII dựa trên kiểm tra trực tiếp tài khoản và kho nguồn Universal Plugin tại thời điểm 2026-09-01 — cần xác minh thêm nếu dùng làm căn cứ quyết định quan trọng.*
