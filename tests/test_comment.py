from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Grievin = User(username = 'Grievin',password = 'potato', email = 'grievin@ms.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="interview",user = self.user_Grievin,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Grievin,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Grievin)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
