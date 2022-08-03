class CommonServices:
    def get_lower_case_str(self, string):
        lower_case_str = ''
        for single_char in string:
            for char in single_char.lower():
                if 97<=ord(char)<=122:
                    lower_case_str += char

    def str_compare(self, str1, str2):
        return True if self.get_lower_case_str(str1) == self.get_lower_case_str(str2) else False