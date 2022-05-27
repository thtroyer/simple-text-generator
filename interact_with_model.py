from textgenrnn import textgenrnn
import os.path


class InteractiveTextGen:
    def __init__(self, model_path):
        self.textgen = self.load_model(model_path)

    def load_model(self, model: str):
        if not os.path.isfile(model):
            raise Exception(f"Can't find model {model}")
        return textgenrnn(model)

    def get_generatated_text(self, prompt: str) -> str:
        return self.textgen.generate(1, temperature=1.0, prefix=prompt)


if __name__ == "__main__":
    interactive = InteractiveTextGen('./interactive_model.hdf5aa')

    print("(Ctrl+c to exit)\n")
    while (True):
        prompt = input("Enter prompt: \n")
        output = interactive.get_generatated_text(prompt)
        print(output)
