import sys
import io
import ddddocr

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

str =b'{"code":"1","desc":"\xe6\x9f\xa5\xe8\xaf\xa2\xe6\x88\x90\xe5\x8a\x9f","request":{"request_status":"04","msg":"\xe6\x93\x8d\xe4\xbd\x9c\xe5\xa4\xb1\xe8\xb4\xa5\xef\xbc\x9a\xe5\xbd\x93\xe5\x89\x8d\xe6\x97\xb6\xe9\x97\xb4\xe4\xb8\x8d\xe5\x85\x81\xe8\xae\xb8\xe8\xae\xa2\xe8\xb4\xa7"}}'


print(str.decode('utf-8'))