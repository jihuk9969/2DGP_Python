***

1. 게임의 소개

	- baba is you.
	- 게임 이미지
	![Title](/termPrj/babaIsYouTitle.jpg "Baba is you 게임의 Title입니다")
	![Game](/termPrj/babaIsYouGameplay.gif "Baba is you 게임의 Gameplay입니다")
	- 게임의 목적, 방법
		- 오브젝트로 된 단어들을 문장으로 만들어 게임을 진행하는 방식

1. Scene : 6개
	
	1. Logo
		- 게임 로고를 띄움
		- 객체 목록
			1. Logo
		- 이벤트
			- SDL_QUIT
	1. Title 
		- 게임 시작 및 종료 가능
		- 객체 목록
			1. TitleBackGround
			1. Start
			1. Exit
		- 이벤트
			- SDL_QUIT
			- 마우스 클릭
			- UI 상호작용
	1. menu
		- 게임 다시시작 및 타이틀로 가는 메뉴 생성
		- 객체목록	
			1. MenuBackGround
			1. Restart
			1. exit
			1. resume
		- 이벤트	
			- SDL_QUIT
			- UI 상호작용
			- 마우스 클릭
			- 키보드 입력
	1. stage1 
		- 튜토리얼
		- 객체 목록
			1. baba
			1. is
			1. you
			1. flag
			1. win
		- 이벤트
			- SDL_QUIT
			- 키보드 입력
	1. stage2 
		- 튜토리얼 2
		- 객체 목록
			1. baba
			1. is
			1. you
			1. flag
			1. win
			1. wall
			1. stop
		- 이벤트
			- SDL_QUIT
			- 키보드 입력
	1. stage3
		- 스테이지 
		- 객체 목록
			1. baba
			1. is
			1. you
			1. flag
			1. win
			1. wall
			1. stop
		- 이벤트
			- SDL_QUIT
			- 키보드 입력
<br>
	- ![StateDiagram](/termPrj/StateDiagram.png "StateDiagram")

	
	

1. 필요한 기술

	- 다른 과목에서 배운 기술
		- 정렬, 탐색, 자료구조
	- 이 과목에서 배울 것으로 기대되는 기술
		- 게임프레임웍, 입자 시스템, 알파 블렌딩
	- 다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술 
		- save, load

***