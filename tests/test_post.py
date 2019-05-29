import unittest
from app.models import User,Post,Comment

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'peels', email = 'james@ms.com')
        self.new_post = Post(id=1234,user_id=6,category='meat',posted_at='5',comments='none')
        self.new_comment = Comment(id=12345,user_id=6, post_id=7, pitch_comment='Eat food',user = self.user_James,post=self.new_post )
        
    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))



    def test_save_post(self):
        self.new_post.save_post()
        posts = Post.query.all()
        self.assertTrue(len(posts)>0)
