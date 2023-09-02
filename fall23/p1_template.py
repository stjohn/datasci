"""
    Name: YOUR NAME HERE (as it appears in Gradescope)
    Email: YOUR EMAIL HERE (as it appears in Gradescope)
    Resources:  ANY RESOURCES YOU USED
"""
import textwrap

def extract_overviews(file_name):
    """
    Opens the file_name and from each line of the file, keeps the overview
    description of the school (the fifth "column": overview_paragraph.
    Returns a list of the paragraphs.
    """

    #Placeholder-- replace with your code
    lst = []
    return lst

def count_lengths(overview_list):
    """
    For each element of the overview_list, computes the length (# of characters).
    Returns the dictionary of length occurrences.
    """

    #Placeholder-- replace with your code
    counts = {}
    return counts

def count_sentences(overview_list):
    """
    For each element of the overview_list, computes the number of periods 
    (as a proxy for the number of sentences).
    Returns the dictionary of occurrences.
    """

    #Placeholder-- replace with your code
    counts = {}
    return counts


def compute_mean(counts):
    """
    Computes the mean of counts dictionary, weighting each key that occurs by its value.
    Returns the mean. 
    """

    #Placeholder-- replace with your code
    mean = 0
    return mean


def compute_mse(theta, counts):
    """
    Computes the Mean Squared Error of the parameter theta and a dictionary, counts.
    Returns the MSE.
    """

    #Placeholder-- replace with your code
    mse = 0

    return mse

def test_compute_mean(mean_fnc=compute_mean):
    """
    Returns True if the mean_fnc performs correctly
    (e.g. computes weighted mean of inputted dictionary) and False otherwise. 
    """

    #Placeholder-- replace with your code
    correct = True
    return correct


def test_mse(mse_fnc=compute_mse):
    """
    Returns True if the extract_fnc performs correctly
    (e.g. computes mean squared error) and False otherwise.
    """

    #Placeholder-- replace with your code
    correct = True
    return correct

def test_count_lengths(counts_fnc=count_lengths):
    """
    Returns True if the counts_fnc performs correctly
    (e.g. counts lengths of overviews and stores in dictionary) & False otherwise.
    """

    #Placeholder-- replace with your code

    correct = True
    return correct


def main():
    """
    Some examples of the functions in use:
    """

    ###Extracts the overviews from the data files:
    file_name = 'fall23/program01/2021_DOE_High_School_Directory_SI.csv'
    si_overviews = extract_overviews(file_name)
    print(f"Number of SI overviews: {len(si_overviews)}. The the last one is:\n")
    #Using textwrap for prettier printing:
    print(textwrap.fill(si_overviews[-1],80))

    late_name = 'fall23/program01/2020_DOE_High_School_Directory_late_start.csv'
    late_overviews = extract_overviews(late_name)
    print(f"\n\nNumber of late start overviews: {len(late_overviews)}. The the last one is:\n")
    print(textwrap.fill(late_overviews[-1],80))

    ###Computing counts and means:
    si_len_counts = count_lengths(si_overviews)
    print(f"The {sum(si_len_counts.values())} entries have lengths:")
    print(si_len_counts)
    late_len_counts = count_lengths(late_overviews)
    print(f"The {sum(late_len_counts.values())} entries have lengths:")
    print(late_len_counts)

    si_dots_counts = count_sentences(si_overviews)
    print(f"The {sum(si_dots_counts.values())} entries have lengths:")
    print(si_dots_counts)
    late_dots_counts = count_sentences(late_overviews)
    print(f"The {sum(late_dots_counts.values())} entries have lengths:")
    print(late_dots_counts)

    si_len_mean = compute_mean(si_len_counts)
    si_dots_mean = compute_mean(si_dots_counts)
    print(f"Staten Island high schools overviews had an average of {si_len_mean:.2f}\
 characters in {si_dots_mean:.2f} sentences.")

    ###Computing MSE:
    late_dots_mean = compute_mean(late_dots_counts)
    print(f"The mean for number of sentences in SI descriptions is {late_dots_mean}.")
    losses = []
    for theta in range(10):
        loss = compute_mse(theta,late_dots_counts)
        print(f"For theta = {theta}, MSE loss is {loss:.2f}.")
        losses.append(loss)

    losses = []
    for theta in range(10):
        loss = compute_mse(theta,si_dots_counts)
        print(f"For theta = {theta}, MSE loss is {loss:.2f}.")
        losses.append(loss)

    ###Testing
    #Trying first on the correct function:
    print(f'test_compute_mean(compute_mean) returns {test_compute_mean(compute_mean)}.')
    #Trying on a function that returns 42 no matter what the output:
    print(f'test_compute_mean( lambda x : 42 ) returns {test_compute_mean(lambda x : 42)}.')



if __name__ == "__main__":
    main()
