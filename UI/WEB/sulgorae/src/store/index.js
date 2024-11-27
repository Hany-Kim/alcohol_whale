import { createStore } from 'vuex'
import { account } from '@/store/modules/account'
import { liquid } from '@/store/modules/liquid'

export default createStore({
  modules: {
    account,
    liquid,
  }
})
