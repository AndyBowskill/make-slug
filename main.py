class MakeSlug(object):
    ''' Slug value (a part of a URL) from a regular sentence. '''

    def check_for_errors(self, sentence):

        error = True
        error_text = None

        self.sentence = sentence

        if self.sentence:
            error = False
        else:
            error_text = "The sentence must be populated. Please try again."

        return error, error_text

    def generate(self):

        slug = self.sentence.lower()
        slug = slug.replace(" ", "-")

        return slug


def main():

    print("Make a slug from sentence you provide.")

    make_slug = MakeSlug()

    error = True

    while error:
        sentence = input("Please enter one sentence: ")
        error, error_text = make_slug.check_for_errors(sentence)
        if error:
            print(error_text)

    slug = make_slug.generate()
    print(f"The generated slug is: {slug}")


if __name__ == "__main__":
    main()