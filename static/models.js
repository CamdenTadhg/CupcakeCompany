class Cupcake {

    constructor({id, flavor, size, rating, image}) {
        this.id = id;
        this.flavor = flavor;
        this.size = size;
        this.rating = rating;
        this.image = image;
    }

    async addCupcake() {
        try{
            console.log('starting submitCupcakeForm');
            const response = await axios.post('/api/cupcakes', cupcakeData)
            console.log(response);
            $cupcakeList.empty();
            getCupcakes();
            $cupcakeFlavorInput.val("");
            $cupcakeSizeInput.val("");
            $cupcakeRatingInput.val("");
            $cupcakeImageInput.val("");
        } catch(error) {
            alert("Form submission failed. Please try again")
        }
    }
}

class CupcakeList {

    constructor(cupcakes){
        this.cupcakes = cupcakes;
    }

    // pulls full list of cupcakes from the api and returns them as an new instance of CupcakeList
    static async getCupcakes() {
        try{
            console.log('starting getCupcakes')
            const response = await axios.get('/api/cupcakes');
            const cupcakes = response.data.cupcakes.map(cupcake => new Cupcake(cupcake));
            return cupcakes;
        } catch(error) {
            alert("No cupcakes found")
        }};
    }
