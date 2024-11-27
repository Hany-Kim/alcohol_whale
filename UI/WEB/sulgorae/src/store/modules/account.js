import router from '@/router'
import axios from 'axios'
import index from '@/api/index'

export const account = {
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: localStorage.getItem('Member_ID') || '',
    currentKiosk: localStorage.getItem('Kiosk_ID') || '',
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    currentKiosk: state => state.currentKiosk,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, Member_ID) => state.currentUser = Member_ID,
    SET_CURRENT_KIOSK: (state, Kiosk_ID) => state.currentKiosk = Kiosk_ID,
  },
  actions: {
    // 인증 정보 저장 및 삭제 기본 함수
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },
    fetchCurrentUser({ commit }, Member_ID) {
      commit('SET_CURRENT_USER', Member_ID)
      localStorage.setItem('Member_ID', Member_ID)
    },
    fetchCurrentKiosk({ commit }, Kiosk_ID) {
      commit('SET_CURRENT_USER', Kiosk_ID)
      localStorage.setItem('Kiosk_ID', Kiosk_ID)
    },

    // 로그인
    // 성공 시 토큰, 현재 유저, 현재 키오스크 저장
    login({ dispatch }, credentials) {
      if (!credentials.Member_ID || !credentials.Password) {
        alert("아이디와 비밀번호를 입력해주세요")
        return
      }
      axios({
        url: index.account.login(),
        method: 'post',
        data: credentials,
        timeout: 2000,
      })
      .then(res => {
        // console.log(res.data);
        dispatch('saveToken', res.data.token || 'success')
        dispatch('fetchCurrentUser', res.data.Member_ID || 'success')
        dispatch('fetchCurrentKiosk', res.data.Kiosk_ID || 'success')
        router.push({ name: 'main' })
      })
      .catch(() => {
        alert("아이디와 비밀번호를 확인해주세요")
        // console.log("fail_login");
        // router.push({ name: 'main' })
        // dispatch('saveToken', 1)
        // dispatch('fetchCurrentUser', 'ssafy6')
        // dispatch('fetchCurrentKiosk', '123456')
      })
    },

    // 로그아웃
    // 현재 토큰 존재 여부 확인 안 함. 수정 필요할 수도.
    logout({ dispatch }) {
      dispatch('removeToken')
      localStorage.clear();
      router.push({ name: 'login' })
    },

    // 회원가입
    // 성공 시 같은 정보로 로그인 요청
    signin({ dispatch }, credentials) {
      if (credentials.Member_ID!==credentials.Member_IDConfirm) {
        alert("아이디 중복 확인을 해주세요.")
        return
      } else if (
          !credentials.Member_ID || !credentials.Password ||
          !credentials.Name || !credentials.Kiosk_ID ||
          !credentials.Phone || !credentials.Email
        ) {
        alert("빈 칸을 모두 입력해주세요")
        return
      } else if (credentials.Password!==credentials.PasswordConfirm) {
        alert("비밀번호와 비밀번호 확인이 다릅니다!")
        return
      }
      axios({
        url: index.account.signin(),
        method: 'post',
        data: credentials,
      })
      .then(() => {
        alert("회원 가입 성공")
        dispatch('login', credentials)
      })
      .catch(() => {
        alert("회원 가입 실패! 다시 시도해주세요.")
      })
    }
  },  
}
