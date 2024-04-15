const getData = () => ({
  regioes: [],
  estados: [],
  cidades: [],
  regiao: '',
  estado: '',
  cidade: '',

  init() {
    this.getRegioes();
    this.getTodosEstados();
    this.getTodasCidades();
  },

  getRegioes() {
    axios.get('/api/v1/regiao')
      .then(response => {
        this.regioes = response.data
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  },

  getEstados(regiao_id) {
    // Filtra Estados
    axios.get(`/api/v1/regiao/${regiao_id}/estados/`)
      .then(response => {
        this.estados = response.data
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
    // Filtra Cidades
    axios.get(`/api/v1/regiao/${regiao_id}/cidades/`)
      .then(response => {
        this.cidades = response.data
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  },

  getTodosEstados() {
    axios.get(`/api/v1/estados/`)
      .then(response => {
        this.estados = response.data
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  },

  getCidades(estado_id) {
    axios.get(`/api/v1/estado/${estado_id}/cidade/`)
      .then(response => {
        this.cidades = response.data
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  },

  getTodasCidades() {
    axios.get('/api/v1/cidades/')
      .then(response => {
        this.cidades = response.data
      })
  },

  getEstadoPorCidade() {
    const cidade_id = this.cidadeSelecionada;
    axios.get(`/api/v1/cidade/${cidade_id}/estado/`)
      .then(response => {
        console.log(response.data[0].nome)
        this.estado = response.data[0].nome
        //this.estados = response.data;
        this.getRegiaoPorEstado(response.data[0].id)
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  },

  getRegiaoPorEstado(estado_id) {
    axios.get(`/api/v1/estado/${estado_id}/regiao/`)
      .then(response => {
        this.regiao = response.data[0].nome
      })
      .catch(error => {
        alert(`Error: ${error}`)
      })
  }
})