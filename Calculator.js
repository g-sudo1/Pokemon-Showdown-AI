// import {calculate, Generations, Pokemon, Move} from '@smogon/calc';
calculate = require("@smogon/calc");
Generations = require("@smogon/calc")
Pokemon = require("@smogon/calc")
Move = require("@smogon/calc")

const gen = 5; // alternatively: const gen = 5;

function testCalculate(){
  calculate(
  gen,
  new Pokemon(gen, 'Gengar', {
    item: 'Choice Specs',
    nature: 'Timid',
    evs: {spa: 252},
    boosts: {spa: 1},
  }),
  new Pokemon(gen, 'Chansey', {
    item: 'Eviolite',
    nature: 'Calm',
    evs: {hp: 252, spd: 252},
  }),
  new Move(gen, 'Focus Blast')
);
}

module.exports = {
  testCalculate: testCalculate
}