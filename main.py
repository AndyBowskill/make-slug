import makeslug


def main():

    print("Make a slug from sentence you provide.")

    error = True

    while error:
        sentence = input("Please enter one sentence: ")
        error, error_text = makeslug.check_for_errors(sentence)
        if error:
            print(error_text)

    slug = makeslug.generate()
    print(f"The generated slug is: {slug}")


if __name__ == "__main__":
    main()
