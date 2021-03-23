import playsound

class SFX:
    __name = ""
    __extension = ""
    __path = ""

    def __init__(self, path, name, extension):
        self.set_path(path)
        self.set_name(name)
        self.set_extension(extension)

    def set_path(self, path):
        """Used to get SFX file path

        Sets private value __path from SFX object using path parameter
        """
        self.__path=path

    def get_path(self):
        """Used to set SFX file path

        Gets private value __path from SFX object and returns through function
        """
        return self.__path

    def get_name(self):
        """Used to get SFX file name

           :returns self.__name
           Gets private value __name from SFX object and returns through function
        """
        return self.__name

    def set_name(self, name):
        """Used to set SFX file name

            :param name
            Sets private value __name from SFX object and returns through function
        """
        self.__name = name

    def set_extension(self, extension):
        """ Used to set SFX file extension

            :param extension
            Sets private flags __MP3 and __WAV based off of extension parameter
        """
        try:
            if(extension != ".mp3"):
                if(extension!=".wav"):
                    raise ValueError
                else:
                    self.__extension = extension
            else:
                self.__extension = extension
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("SFX Extension must be .wav or .mp3. Extension unchanged.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def get_extension(self):
        """ Used to get SFX file extension

            Returns string based off of extension flags
        """
        return self.__extension

    def play(self):
        fullName = self.__path + self.__name + self.get_extension()
        playsound.playsound(fullName)


