# JSON
import json

d = dict(name='Bob', age=20, score=88)
# print(json.dump(d))

# JSON反序列化用loads()
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
