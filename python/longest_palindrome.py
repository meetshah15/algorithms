class Solution:

    def longestPalindrome(self, s: str) -> str:
        count = 0
        answer = ''

        for index, letter in enumerate(s):
            for sub_index in range(index, len(s)):
                text = s[index: sub_index+1]
                if len(text) > count and text == text[::-1]:
                    answer = text
                    count = len(text)

            if len(answer) == len(s):
                break

        return answer


if __name__ == '__main__':
    solution = Solution()
    # answer = solution.longestPalindrome("qagtxztpovdbqrhtftxrfjkrrjnhbkoawjctdiaygmbutzzosisyxwqbufsgbmfbpcxvdibnayximkkdmviorabhjasxyyagqrxzfewimqewftfihlgsqmkoapwckbhdarhlbonypdzhnxcnzanlrjzfixrpepsjmdepgxvyuijonhqnejymwlofzskcfqdyyfowkzhswutsuhwiqkoogeqkcpjrqndeaxqvdadheostwdonphfaemebuqmwdtrioyjtzoprasizwmwfikaihudneusfgdtcpwgzkwnceziayflxrsmydjiwbeqdzcfewedulydcoahgptzzlzldzaazblvzxuvdxhmzbwasfibtkxuylpklpbfmhujcwvmhbylkrxmhgmmrzdanhsvkrlwqctoexcmhughsvcqgdxxnvcawrroebqylnelyodxfkrplprldsjeejsdlrplprkfxdoylenlyqbeorrwacvnxxdgqcvshguhmcxeotcqwlrkvshnadzrmmghmxrklybhmvwcjuhmfbplkplyuxktbifsawbzmhxdvuxzvlbzaazdlzlzztpghaocdyludewefczdqebwijdymsrxlfyaizecnwkzgwpctdgfsuenduhiakifwmwzisarpoztjyoirtdwmqubemeafhpnodwtsoehdadvqxaednqrjpckqegookqiwhustuwshzkwofyydqfckszfolwmyjenqhnojiuyvxgpedmjspeprxifzjrlnazncxnhzdpynoblhradhbkcwpaokmqsglhiftfweqmiwefzxrqgayyxsajhbaroivmdkkmixyanbidvxcpbfmbgsfubqwxysisozztubmgyaidtcjwaokbhnjrrkjfrxtfthrqbdvoptzxtgaq")
    answer = solution.longestPalindrome("babad")
    print(answer)

