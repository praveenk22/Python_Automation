def search(text_, pattern_):
    '''
    This function implements naive search algorithm.
    '''

    M = len(pattern_)
    N = len(text_)


    #Loop through starting of text_ till the stretch where the pattern_ can be checked completely in text_
    for i in range(N - M + 1):
        j = 0

        #Loop through pattern_ and compare letter by letter.
        for j in range( 0, M ):

            if text_[ i + j ] != pattern_[j]:
                break

            if (j == M - 1):
                print("Pattern found at index:", i)

if __name__ == "__main__":
    txt= "BDOGCATDOG"
    pat = "DOG"
    search( txt, pat )
