class Book:

    def __init__(self, title, author, publisher):
        ##Using set methods to initialize the data.
        self.__setTitle(title)
        self.__setAuthorName(author)
        self.__setPublisherName(publisher)

    ##Mutators
    def __setTitle(self, title):
        self.__title = title

    def __setAuthorName(self, name):
        self.__author = name

    def __setPublisherName(self, publisher):
        self.__publisher = publisher
        
    ##Accessors
    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        return self.__author
    
    def getPublisher(self):
        return self.__publisher

    def __str__(self):
        return "Book title: {0}\nAuthor's Name: {1}\nPublisher's Name: {2}".format(self.getTitle(),
                                                                                self.getAuthor(),
                                                                                self.getPublisher())
#this was for testing only, not pert of assignment (hence the commenting out)
##def main():
##    book = Book("Mistborn", "Sanderson", "Tor")
##
##    print(str(book))
##
##    
##main()
