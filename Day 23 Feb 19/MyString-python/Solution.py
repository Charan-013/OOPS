import re

class MyString:
    def __init__(self, String=""):
        if String == "":
            self.string = ""
        elif isinstance(String, list):
            self.string = "".join(String)
        elif isinstance(String, MyString):
            self.string = String.string

    def length(self):
        return len(self.string)

    def char_at(self, idx):
        return self.string[idx]

    def substring(self, bidx, eidx=None):
        if eidx == None:
            return self.string[bidx:]
        return self.string[bidx:eidx]

    def compare_to(self, other):
        count = 0
        for i in range(min(len(self.string), len(other.string))):
            if self.string[i] != other.string[i]:
                count -= 1
        return count

    def compare_to_ignore_case(self, other):
        count = 0
        for i in range(min(len(self.string), len(other.string))):
            if self.string[i].lower() != other.string[i].lower():
                count -= 1
        return count
        pass

    def equals_ignore_case(self, other):
        count = 0
        for i in range(min(len(self.string), len(other.string))):
            if self.string[i].lower() != other.string[i].lower():
                count -= 1
        return count == 0
        pass

    def concat(self, s):
        new_str = self.string + s.string
        return new_str

    def replace(self, old, new):
        new_str = ""
        for i in range(len(self.string)):
            if self.string[i] == old:
                new_str += new
            else:
                new_str += self.string[i]
        return new_str

    def replace_seq(self, old, new):
        string = self.string
        new_string = string.split(old.string)
        return new.string.join(new_string)

    def replace_all(self, regex, replacement):
        m = re.sub(regex, replacement.string, self.string)
        return m

    def replace_first(self, regex, replacement):
        m = re.sub(regex, replacement.string, self.string, count=1)
        return m

    def contains(self, s):
        if s.string in self.string:
            return True
        return False

    def index_of(self, c):
        if isinstance(c, MyString):
            for i in range(len(self.string) - len(c.string) + 1):
                if self.string[i : i + len(c.string)] == c.string:
                    return i
            return -1
        else:
            for i in range(len(self.string)):
                if self.string[i] == c:
                    return i
            return -1

    def index_of_from(self, c, idx):
        if isinstance(c, MyString):
            for i in range(idx, len(self.string) - len(c.string) + 1):
                if self.string[i : i + len(c.string)] == c.string:
                    return i
            return -1
        else:
            for i in range(idx, len(self.string)):
                if self.string[i] == c:
                    return i
            return -1

    def last_index_of(self, c):
        if isinstance(c, MyString):
            for i in range(len(self.string) - len(c.string), -1, -1):
                if self.string[i : i + len(c.string)] == c.string:
                    return i
            return -1
        else:
            for i in range(len(self.string) - 1, -1, -1):
                if self.string[i] == c:
                    return i
            return -1

    def last_index_of_from(self, c, idx):
        if isinstance(c, MyString):
            return self.string.rfind(c.string, idx) - 1
        # else:
        #     return self.string.rfind(c, 0, idx)
        for i in range(len(self.string) - 1, -1, -1):
            if self.string[i] == c:
                return i - 1
        return -1

    def is_empty(self):
        return len(self.string) == 0

    def to_char_array(self):
        return list(self.string)

    def to_lower_case(self):
        lower_str = ""
        for char in self.string:
            if "A" <= char <= "Z":
                lower_str += chr(ord(char) + 32)
            else:
                lower_str += char
        return lower_str

    def to_upper_case(self):
        upper_str = ""
        for char in self.string:
            if "a" <= char <= "z":
                upper_str += chr(ord(char) - 32)
            else:
                upper_str += char
        return upper_str

    def trim(self):
        return self.string.strip()

    def starts_with(self, s):
        if self.string.find(s.string) == 0:
            return True
        return False
        

    def starts_with_from(self, s, idx):
        if self.string.find(s.string) == idx:
            return True
        return False

    def split(self, d):
        return self.string.split(d.string)

    def split_limit(self, d, l):
        return self.string.split(d.string, l - 1)

    def __str__(self):
        return self.string
