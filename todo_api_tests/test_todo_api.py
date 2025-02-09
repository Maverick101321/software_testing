import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io/'

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_tasks():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    #create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    #update a task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "new content",
        "is_done": True,
    }
    assert update_task(new_payload).status_code == 200
    #get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]
    
def test_can_list_tasks():
    #creating n tasks
    n=5
    payload = new_task_payload()
    for i in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    #listing tasks and checking if there's n tasks
    user_id = payload["user_id"]
    list_tasks_response = list_tasks(user_id)
    assert list_tasks_response.status_code == 200
    list_tasks_data = list_tasks_response.json()
    print(list_tasks_data)

    tasks = list_tasks_data["tasks"]
    assert len(tasks) == n

def test_can_delete_task():
    #create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    #delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    #get the task and check that its not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    print (f"Creating task for user {user_id} with content {content}")
    return {
        "content" : content,
        "user_id" : user_id,
        "is_done" : False
    }
