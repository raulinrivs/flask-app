from car_registration import create_app


def test_owner_page():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('/owner')
        assert response.status_code == 200
        
def test_car_page():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('/car')
        assert response.status_code == 200