'''
단어장 관리 프로그램 다음 메뉴를 이용하여 동작하는 프로그램
1. 단어 입력
2. 단어 수정
3. 단어 삭제
4. 단어 검색
5. 단어장 전체 출력
0. 종료
'''
MAX = 50
WORD_LENGTH = 10
CLASS_LENGTH = 5
MEANING_LENGTH = 20
wordbook = {}
count = 0

def word_input():
    MAX = 50
    WORD_LENGTH = 10
    CLASS_LENGTH = 5
    MEANING_LENGTH = 20
    wordbook = {}
    count = 0
    word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    while len( word_name ) < 1 or len( word_name ) > WORD_LENGTH:
        print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
        word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
            
    while word_name != 'end' and count < MAX:
        count = count + 1
        word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )
        while len( word_class ) < 1 or len( word_class ) > CLASS_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( CLASS_LENGTH ) )
            word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )

        word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )
        while len( word_meaning ) < 1 or len( word_meaning ) > MEANING_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( MEANING_LENGTH ) )
            word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )

        word = ( word_name, word_class, word_meaning )
        wordbook[ word_name ] = word    
        
        word_name = input( '\n최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
        while len( word_name ) < 1 or len( word_name ) > WORD_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
            word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )

    return wordbook
    
if __name__ == '__main__' :    
totalword = word_input()
print(totalword)