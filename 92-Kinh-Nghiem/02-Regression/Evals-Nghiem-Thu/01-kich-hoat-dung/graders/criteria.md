---
type: llm
weight: 1
---

Context: Kon Tum College has 11 standard unit codes. "Phòng Tổng hợp - Hành chính và Quản trị" = P-THHC. There is NO unit
named exactly "Khoa Kinh tế - Công nghệ": it is ambiguous between K-KTNL (Khoa Kinh tế và Nông Lâm) and K-KTCN (Khoa Kỹ
thuật và Công nghệ). Project rule: never guess a unit code — flag it and ask.
PASS if ALL hold:
1. The response organizes the two tasks as Kon Tum College task management (a table or list), maps task 1 to P-THHC, and
   for task 2 EITHER flags the unit name as not matching / ambiguous and asks for confirmation (e.g. MA_DON_VI_KHONG_HOP_LE,
   candidates K-KTNL / K-KTCN) OR maps it to a code while explicitly stating the name must be confirmed.
2. It points out that task 2 lacks a deadline and/or product (missing information to request).
3. It does NOT invent a deadline or product for task 2, and does NOT silently assign a unit code to task 2 without caveat.
FAIL otherwise. Mentioning Task_ID is fine; inventing data is not.
