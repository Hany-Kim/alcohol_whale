const HOST = 'http://i7a106.p.ssafy.io:8000/'

const MAIN = 'main/'
const REQUEST = 'request/'

export default {
  account: {
    // 로그인
    login: () => HOST + 'login/',
    
    // 회원가입
    signin: () => HOST + 'signin/',
    
    // ID 중복 검사
    idconfirm: (Member_ID) => HOST + 'id_check/'+`${Member_ID}/`,
  },

  main: {
    // 재고 DB 정보 받아오기
    inventory: (Kiosk_ID) => HOST + MAIN + `${Kiosk_ID}/`,

    // // 단일 주류 받아오기(쓸 일 없을 듯)
    // liquid: (Kiosk_ID, Liq_ID) => HOST + MAIN + `${Kiosk_ID}/info/${Liq_ID}/`,

    // 재고 DB 주류 수정
    editLiquid: (Kiosk_ID) => HOST + MAIN + `${Kiosk_ID}/info/edit/`,
    
    // 재고 DB 검색 
    searchDB: (Kiosk_ID) => HOST + MAIN + `${Kiosk_ID}/search/`,

    // 재고 DB 신규 주류 추가
    addLiquid: (Kiosk_ID, Liq_ID) => HOST + MAIN + `${Kiosk_ID}/add/${Liq_ID}/`,

    // // 재고 단일 주류 삭제 (쓸 일 없을 듯)
    // deleteLiquid: (Kiosk_ID, Liq_ID) => HOST + MAIN + `${Kiosk_ID}/delete/${Liq_ID}/`,

    // 재고 DB 신규 주류 추가 위한 검색
    searchForAdd: (Kiosk_ID,Liquor_Name) => HOST + MAIN + `${Kiosk_ID}/add_get/${Liquor_Name}/`,

    // graph 데이터 요청
    graph: (Kiosk_ID,category) => HOST + `graph/${Kiosk_ID}/${category}/`,

    // Admin에게 주류 DB 관련 요청
    request: () => HOST + REQUEST
  },
}