from app import app, db, Post
from datetime import datetime

def init_db():
    with app.app_context():
        # Drop all existing tables
        db.drop_all()
        # Create all tables
        db.create_all()
        
        # Create some sample posts
        sample_posts = [
            {
                'title': 'Your most unhappy customers are your greatest source of learning.',
                'content': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.',
                'category': 'Business',
                'author_name': 'Sergy Campbell',
                'author_title': 'CEO and Founder',
                'image_url': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=800&h=600'
            },
            {
                'title': 'The future of sustainable technology',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                'category': 'Technology',
                'author_name': 'Emma Watson',
                'author_title': 'Tech Lead',
                'image_url': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&h=600'
            },
            {
                'title': 'Exploring hidden gems in nature',
                'content': 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                'category': 'Travel',
                'author_name': 'John Smith',
                'author_title': 'Travel Writer',
                'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&h=600'
            }
        ]

        # Add sample posts to database
        for post_data in sample_posts:
            post = Post(**post_data)
            db.session.add(post)

        # Commit the changes
        db.session.commit()

if __name__ == '__main__':
    init_db()
