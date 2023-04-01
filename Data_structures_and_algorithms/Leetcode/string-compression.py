class Solution:
    def compress(self, chars: list[str]) -> int:
        chars.append(None)
        s = ""
        cur_char = chars[0]
        chars_num = 0
        for i in range(1, len(chars)):
            chars_num += 1
            if chars[i] != chars[i - 1]:
                s += (cur_char + ("" if chars_num == 1 else str(chars_num)))
                cur_char = chars[i]
                chars_num = 0
        chars.clear()
        cur_count = ""
        all_count = 0
        while s != '':
            chars += [s[:1]]
            all_count += 1
            if s[:1].isdigit():
                cur_count += s[:1]
            else:
                all_count += 0 if (cur_count == "" or len(cur_count) == 1) else int(cur_count)
                cur_count = ""
            s = s[1:]
        return all_count
