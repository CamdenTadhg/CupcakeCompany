class Cupcake {

    constructor({id, flavor, size, rating, image}) {
        this.id = id;
        this.flavor = flavor;
        this.size = size;
        this.rating = rating;
        this.image = image;
    }

    //create a new instance of cupcake and add it to the database. 
    async addCupcake() {
        try{
            console.log('starting add cupcake');
            const response = await axios.post('/api/cupcakes', cupcakeData)
            console.log(response);
            $cupcakeList.empty();
            mainCupcakeList = await CupcakeList.getCupcakes();
            displayCupcakes(mainCupcakeList);
            $cupcakeFlavorInput.val("");
            $cupcakeSizeInput.val("");
            $cupcakeRatingInput.val("");
            $cupcakeImageInput.val("");
        } catch(error) {
            alert("Form submission failed. Please try again")
        }
    }

    static async deleteCupcake(cupcakeId){
        try{
            console.log('starting delete cupcake');
            await axios.delete(`/api/cupcakes/${cupcakeId}`);
        } catch(error) {
            alert("Delete cupcake failed. Please try again.")
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
            return new CupcakeList(cupcakes);
        } catch(error) {
            alert("No cupcakes found")
        }};

    //search for cupcakes matching an inputted search string and return an instance of CupcakeList
    static searchCupcakes(searchTerm){
        const numericSearchTerm = parseInt(searchTerm);
        const cupcakeResults = [];
        for (let cupcake of mainCupcakeList.cupcakes){
            console.log('CUPCAKE = ', cupcake);
            for (let key in cupcake){
                console.log(key);
                //searches numeric values for the appropriate keys
                if (key === 'id' || key === 'rating'){
                    console.log(cupcake[key]);
                    if (cupcake[key] === numericSearchTerm){
                        if (cupcakeResults.includes(cupcake) === false){
                            cupcakeResults.push(cupcake);
                            console.log('CUPCAKE ADDED');
                        }
                    }
                }
                //searches string values for the remaining keys
                else if (key === "flavor" || key === "size"){
                    if (cupcake[key].toLowerCase().search(searchTerm.toLowerCase()) != -1){
                        if (cupcakeResults.includes(cupcake) === false){
                            cupcakeResults.push(cupcake);
                            console.log('CUPCAKE ADDED');
                        }
                    }
                }
            }
        }
        console.log(cupcakeResults);
        return new CupcakeList(cupcakeResults);
    }

    }
