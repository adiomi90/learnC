const person = {
    name: ["Bob", "smith"],
    age : 32,
    bio: function () {
        console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old`);
    },
    introductSelf: function () {
        console.log(`Hi! I'm ${this.name[0]}`)
    },

};



person.bio()
person.introductSelf()