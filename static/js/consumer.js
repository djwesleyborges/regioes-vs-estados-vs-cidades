const getData = () => ({
    regioes: [],
    estados: [],
    cidades: [],
    regiaoSelecionada: null,
    estadoSelecionado: null,
    cidadeSelecionada: null,
    regiao: '',
    estado: '',
    cidade: '',


    init() {
        this.getRegioes();
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
    getEstados() {
        const regiao_id = this.regiaoSelecionada;
        axios.get(`/api/v1/regiao/${regiao_id}/estados/`)
            .then(response => {
                this.estados = response.data
            })
            .catch(error => {
                alert(`Error: ${error}`)
            })
    },
    getCidades() {
        const estado_id = this.estadoSelecionado;
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