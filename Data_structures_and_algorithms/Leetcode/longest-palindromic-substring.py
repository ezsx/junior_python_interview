class polindrom:

    def __init__(self, s: str, lb: int, rb: int):
        self.s = s
        self.lb = lb
        self.rb = rb
        self.len = 0

    def __len__(self):
        return self.len

    def __repr__(self):
        return self.s[self.lb:self.rb + 1]

    def set_len(self):
        while self.lb > 0 and self.rb < len(self.s) - 1:
            if self.s[self.lb - 1] == self.s[self.rb + 1]:
                self.lb -= 1
                self.rb += 1
            else:
                break
        self.len = self.rb - self.lb + 1


def get_len_str(s, lb, rb):
    while lb > 0 and rb < len(s) - 1:
        if s[lb - 1] == s[rb + 1]:
            lb -= 1
            rb += 1
        else:
            break
    return rb - lb + 1, s[lb:rb + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if all(elem == s[0] for elem in s):
        #     return s
        len_max = 0
        pol_max = s[0]
        len_s = len(s)
        for i in range(len_s):
            for r in (1, 2):
                if (i < len_s - r) and s[i] == s[i+r]:
                    #len_p, s_p = get_len_str(s, i, i+r)
                    lb = i
                    rb = i+r
                    while lb > 0 and rb < len(s) - 1:
                        if s[lb - 1] == s[rb + 1]:
                            lb -= 1
                            rb += 1
                        else:
                            break

                    if rb - lb + 1 > len_max:
                        len_max = rb - lb + 1
                        pol_max = s[lb:rb + 1]
        return pol_max

cs = []
cs.append("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")
cs.append("caaaaa")
cs.append("ac")
cs.append(("abb"))
for s in cs:
    print(Solution().longestPalindrome(s))
