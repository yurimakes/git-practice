# Git 명령어 정리

7주차 수업에서 사용한 명령어를 기억하기 위해 정리했다.

| 명령어 | 의미 |
| --- | --- |
| `git init` | 현재 폴더를 Git 저장소로 만든다. |
| `git status` | 파일의 현재 상태를 확인한다. |
| `git add main.py` | 지정한 파일을 staging area에 올린다. |
| `git add .` | 현재 폴더의 변경 파일을 한꺼번에 올린다. |
| `git commit -m "message"` | stage에 올린 변경 사항을 기록한다. |
| `git log` | 지금까지의 커밋 기록을 확인한다. |
| `git mv old.txt new.txt` | Git이 관리하는 파일의 이름을 바꾼다. |
| `git rm file.txt` | 추적하는 파일을 삭제하고 삭제 내역을 stage에 올린다. |
| `git push -u origin main` | 로컬 main 브랜치를 원격 저장소로 올린다. |

`git add`만 했을 때는 커밋이 만들어지지 않는다. `git commit`까지 해야 하나의 기록으로 남는다.
