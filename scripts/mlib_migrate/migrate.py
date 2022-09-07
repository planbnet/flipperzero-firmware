#!/usr/bin/env python3

header_in_path = "m-string.h"
header_out_path = "../../lib/mlib/m-string.h"
source_out_path = "../../lib/mlib/m-string.c"


def main():
    header_in_file = open(header_in_path, "rt")
    header_out_file = open(header_out_path, "w")
    source_out_file = open(source_out_path, "w")

    source_out_file.writelines('#include "m-string.h"\r\n')
    source_out_file.writelines("#pragma GCC diagnostic push\r\n")
    source_out_file.writelines(
        '#pragma GCC diagnostic ignored "-Wunused-parameter"\r\n'
    )
    source_out_file.writelines("\r\n")
    source_out_file.writelines("#undef string_set\r\n")
    source_out_file.writelines("#undef string_init_set\r\n")
    source_out_file.writelines("#undef string_cat\r\n")
    source_out_file.writelines("#undef string_cmp\r\n")
    source_out_file.writelines("#undef string_equal_p\r\n")
    source_out_file.writelines("#undef string_search_char\r\n")
    source_out_file.writelines("#undef string_search_rchar\r\n")
    source_out_file.writelines("#undef string_search_str\r\n")
    source_out_file.writelines("#undef string_search\r\n")
    source_out_file.writelines("#undef string_search_pbrk\r\n")
    source_out_file.writelines("#undef string_strcoll\r\n")
    source_out_file.writelines("#undef string_replace_str\r\n")
    source_out_file.writelines("#undef string_replace\r\n")
    source_out_file.writelines("#undef string_strim\r\n")
    source_out_file.writelines("\r\n")

    while True:
        line = header_in_file.readline()
        text = ""
        fn_text = ""
        if not line:
            break

        if line.startswith("static inline "):
            text += line
            line = header_in_file.readline()
            if line.startswith("string_"):
                text += line
                text = text.replace("static inline ", "")
                fn_text = text
                source = True

                fn_stack = 0
                while True:
                    line = header_in_file.readline()
                    if line.startswith("{"):
                        fn_stack += 1
                    elif line.startswith("}"):
                        fn_stack -= 1
                    text += line
                    if fn_stack == 0:
                        break

                line = ""

        if fn_text:
            header_out_file.writelines(
                '#ifdef __cplusplus\r\n extern "C" {\r\n#endif\r\n'
            )
            fn_text = fn_text.replace("\r", "")
            fn_text = fn_text.replace("\n", " ")
            fn_text += ";\r\n"
            header_out_file.writelines(fn_text)
            header_out_file.writelines("#ifdef __cplusplus\r\n }\r\n#endif\r\n")

            source_out_file.writelines(text)
            source_out_file.writelines("\r\n")
        else:
            header_out_file.writelines(text)
            header_out_file.writelines(line)

    source_out_file.writelines("#pragma GCC diagnostic pop\r\n")


if __name__ == "__main__":
    main()
