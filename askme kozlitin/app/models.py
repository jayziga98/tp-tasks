from django.db import models

USERS = [
    {'id': 0, 'login': 'login_guest', 'email': 'guest@mail.ru', 'is_auth': False, 'nickname': 'guest', 'avatar': 'img/guest_avatar.png'}
]

USERS += [
    {
        'id': user_id,
        'login': f'user_{user_id}_login',
        'email': f'user_{user_id}@mail.ru',
        'is_auth': True,
        'nickname': f'User_{user_id}',
        'avatar': f'img/user_{user_id}_avatar.jpeg'
    } for user_id in range(1, 5)
]

TAGS = [
    {
        'id': tag_id,
        'name': f'tag_{tag_id}',
    } for tag_id in range(100)
]

QUESTIONS = [
    {
        'id': question_id,
        'user': USERS[question_id % 5],
        'title': f'Question {question_id}',
        'content': f'question number {question_id} content',
        'answers': [
            {
                'id': answer_id,
                'user': USERS[(answer_id * 3) % 5],
                'title': f'Answer {answer_id}',
                'content': f'answer number {answer_id} content',
                'is_correct': False,
            } for answer_id in range(question_id)
        ],
        'tags': [TAGS[i] for i in range(question_id)],
    } for question_id in range(100)
]
