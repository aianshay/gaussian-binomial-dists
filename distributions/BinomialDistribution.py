import matplotlib.pyplot as plt
import numpy as np
from .GeneralDistribution import Distribution
from math import factorial
import seaborn as sns


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) size of the distribution
                
    """

    def __init__(self, probability=0.5, size=10):
        self.p = probability
        self.n = size
        
    
    def calculate_mean(self): 
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n
        return self.mean
         

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = np.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
    
    
    def replace_stats_with_data(self): 
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """

        self.p = sum(self.data)/len(self.data)
        self.n = len(self.data)
        return self.p, self.n


    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        labels = ['tails', 'heads']
        heads = sum(self.data)
        tails = len(self.data) - heads
        
        sns.barplot(x=labels, y=[tails, heads], ci=None)
        plt.title('Histogram of Data')
        plt.ylabel('Ocurrences')


    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        combination = factorial(self.n)/(factorial(self.n - k) * factorial(k))
        pdf = combination * self.p**k * (1 - self.p)**(self.n - k)
        return pdf 


    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        n = list(range(self.n))
        k = [self.pdf(k) for k in n]
        sns.barplot(x=n, y=k, ci=None)
        plt.title('Probability density function of k')
        plt.ylabel('PDF(k)')
        plt.xlabel('k')
        return n, k 
       

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        binomial = Binomial(self.p, self.n + other.n)
        return binomial
    

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
    
        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}.1f, n {self.n}'
