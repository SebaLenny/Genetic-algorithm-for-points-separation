# Genetic-algorithm-for-points-separation

The goal of our Genetic Algorithm is to find a polynomial that will separate 2 types of points by keeping one type above and one type below the function curve.

## Chromosome

Each chromosome is defined as an vector of coefficients of polynomial

## Mutation

In my approach after generation of population each gene is mutating by adding a value from normal distribution (probability density function) modulated by parameter sigma. The rule is easy, bigger sigma parameters yields more aggressive mutations and vice versa.

## Crossover

The sole purpose of crossover function in my algorithm is to generate new chromosomes, not to crossover existing ones. My version of crossover is adapted 3 parent algorithm where three parents are picked that produce one offspring that takes each gene from randomly selected parent.

## Selection

My selection method for creating new generation is quite simple. First I defined selector that takes “n” chromosomes from sorted based on fitness population using 1x+1probability distribution. That way of selecting preferes better chromosomes but still have quite significant chance of picking worse ones. Using that selector i pick portion of old generation for breeding the new one.

### Sample point space
![Sample points for 1st problem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/points.png)<br />
### Obtainded polynomial
![Result for 1st problem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/results1.png)<br />
### Statistics regarding algorithm progress
GA was able to find “desired” polynomial within 13 generations. Generally over generations the average and best fitness was going down which was expected. Algorithm found local minimum at 4th generation but thanks to the mutation was able to search for wider space and eventually find solution. 
Mutation coefficient is not changing over time this is risky strategy and if we need fine tuned polynomials that might be an issue. 
On average GA with this set of points and parameters is able to find “desired” polynomial within 20 generations.<br />
![Stats for 1st prbolem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/stats1.png)<br />
### Sample overlapping point space
![Sample points for 2nd problem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/points2.png)<br />
### Obtainded polynomial
![Result for 2nd problem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/results2.png)<br />
### Statistics regarding algorithm progress
We can observe that that best fitness settles in about 20 generations, the searching stops at 125 because it didn’t found “perfect” solution due to overlapping of sets. Good idea would be to use standard deviation to know if the algorithm in not developing anymore.<br />
![Stats for 2nd prbolem](https://github.com/SebaLenny/Genetic-algorithm-for-points-separation/blob/master/stats2.png)<br />
