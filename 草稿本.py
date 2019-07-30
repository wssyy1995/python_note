class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def story_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        count=1
        print('survey results:')
        for i in self.responses:
            print(str(count) +':'+ i)
            count+=1



# question='what language did you first learn to speak'
# mysurvey=AnonymousSurvey(question)
# mysurvey.show_question()
# print('enter q at any time to quit.\n')
# while True:
#     response=input('my response:')
#     if response =='q':break
#     mysurvey.story_response(response)
#
# mysurvey.show_results()



import unittest
class TestAnonymousSurvey(unittest.TestCase):


    def setUp(self):
        question = 'what language did you first learn to speak'
        self.mysurvey= AnonymousSurvey(question)

    def test_sotre_single_response(self):
        response = 'English'
        self.mysurvey.story_response(response)
        self.assertIn(response, self.mysurvey.responses)

    def test_store_three_responses(self):

        responses=['english','spanish','mandarin']
        for response in responses:
            self.mysurvey.story_response(response)

        for response in responses:
            self.assertIn(response,self.mysurvey.responses)

unittest.main()
