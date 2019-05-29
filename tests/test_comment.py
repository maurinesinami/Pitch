import unittest
from app.models import Comment, User,Post
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'peels', email = 'james@ms.com')
        self.new_post = Post(id=1234,user_id=6,category='meat',posted_at='5',comments='none')
        self.new_comment = Comment(id=12345,user_id=6, post_id=7, pitch_comment='Eat food',user = self.user_James,post=self.new_post )
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.user_id,6)
        self.assertEquals(self.new_comment.post_id,7)
        self.assertEquals(self.new_comment.pitch_comment,'Eat food')
        self.assertEquals(self.new_comment.user,self.user_James,self.new_post)


    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.query.all()
        self.assertTrue(len(comments)>0)


    
