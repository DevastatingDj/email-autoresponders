with open("KnowledgeBase.txt") as kb:
    qna = kb.readlines()
qna = [x.strip() for x in qna]

try:
    for j in range(len(qna)):
        if '' in qna:
            qna.remove('')
        if '\n' in qna:
            qna.remove('\n')
except IndexError:
    pass


def get_question_answers():
    """Returns questions and answers from KnowledgeBase.txt"""

    questions = []
    answers = []

    for i in range(len(qna)):
        if i % 2 == 0:
            questions.append(qna[i])
        else:
            answers.append(qna[i])
    return [questions, answers]
