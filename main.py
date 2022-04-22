import plotly.graph_objs as go
from utils import print_bst_to_json, generate_trees, get_averages, input_checker, read_bst_from_json, split_and_filter

def main():
    # the graph that will show no matter what option people choose: comparing average positive compound score
    # with average negative compound score for all categories together
    # the specific option one will be the 10 most used words in all tweets found and their frequencies in the tweets
    cops, state_violence, police_violence, police_brutality, police_misconduct = generate_trees()
    print_bst_to_json('cops_tree.json', cops)
    print_bst_to_json('state_violence_tree.json', state_violence)
    print_bst_to_json('police_violence_tree.json', police_violence)
    print_bst_to_json('police_brutality_tree.json', police_brutality)
    print_bst_to_json('police_misconduct_tree.json', police_misconduct)
    print("Welcome! This interactive program will analyze tweets related to the following 5 subjects:\n")
    print("Cops\nState Violence\nPolice Violence\nPolice Brutality\nPolice Misconduct\n")
    contin = True
    while contin == True:
        print("If you would like to exit out of this program, type 'quit' at this point")
        query = input_checker()
        if query == 'quit':
            contin = False
            break
        xvals = ['cops negative', 'state violence negative', 'police violence negative', 'police brutality negative', 'police misconduct negative', 'cops positive', 'state violence positive', 'police violence positive', 'police brutality positive', 'police misconduct positive']
        yvals = []
        cops_data = read_bst_from_json('cops_tree.json')
        state_violence_data = read_bst_from_json('state_violence_tree.json')
        police_violence_data = read_bst_from_json('police_violence_tree.json')
        police_brutality_data = read_bst_from_json('police_brutality_tree.json')
        police_misconduct_data = read_bst_from_json('police_misconduct_tree.json')
        cop_neg = 0
        cop_pos = 0
        state_neg = 0
        state_pos = 0
        police_vio_neg = 0
        police_vio_pos = 0
        police_brut_neg = 0
        police_brut_pos = 0
        police_mis_pos = 0
        police_mis_neg = 0
        cop_neg, cop_pos = get_averages(cops_data, cop_neg, cop_pos)
        state_neg, state_pos = get_averages(state_violence_data, state_neg, state_pos)
        police_vio_neg, police_vio_pos = get_averages(police_violence_data, police_vio_neg, police_vio_pos)
        police_brut_neg, police_brut_pos = get_averages(police_brutality_data, police_brut_neg, police_brut_pos)
        police_mis_neg, police_mis_pos = get_averages(police_misconduct_data, police_mis_neg, police_mis_pos)
        yvals.append(cop_neg/len(cops_data))
        yvals.append(state_neg/len(state_violence_data))
        yvals.append(police_vio_neg/len(police_violence_data))
        yvals.append(police_brut_neg/len(police_brutality_data))
        yvals.append(police_mis_neg/len(police_misconduct_data))
        yvals.append(cop_pos/len(cops_data))
        yvals.append(state_pos/len(state_violence_data))
        yvals.append(police_vio_pos/len(police_violence_data))
        yvals.append(police_brut_pos/len(police_brutality_data))
        yvals.append(police_mis_pos/len(police_misconduct_data))
        bar_data = go.Bar(x=xvals, y=yvals)
        basic_layout = go.Layout(title="Comparison of average positivity and negativity compound scores for each query group")
        fig = go.Figure(data=bar_data, layout=basic_layout)
        fig.show()
        xvals.clear()
        yvals.clear()
        if query == 'cops':
            cop_words = split_and_filter(cops_data)
            for word in cop_words:
                xvals.append(word[0])
                yvals.append(word[1])
            bar_data = go.Bar(x=xvals, y=yvals)
            basic_layout = go.Layout(title="Ten Most Common Words in 'Cops' Query")
            fig=go.Figure(data=bar_data, layout=basic_layout)
            fig.show()
            xvals.clear()
            yvals.clear()
        elif query == 'state violence':
            state_words = split_and_filter(state_violence_data)
            for word in state_words:
                xvals.append(word[0])
                yvals.append(word[1])
            bar_data = go.Bar(x=xvals, y=yvals)
            basic_layout = go.Layout(title="Ten Most Common Words in 'State Violence' Query")
            fig=go.Figure(data=bar_data, layout=basic_layout)
            fig.show()
            xvals.clear()
            yvals.clear()
        elif query == 'police violence':
            police_vio_words = split_and_filter(police_violence_data)
            for word in police_vio_words:
                xvals.append(word[0])
                yvals.append(word[1])
            bar_data = go.Bar(x=xvals, y=yvals)
            basic_layout = go.Layout(title="Ten Most Common Words in 'Police Violence' Query")
            fig=go.Figure(data=bar_data, layout=basic_layout)
            fig.show()
            xvals.clear()
            yvals.clear()
        elif query == 'police brutality':
            brut_words = split_and_filter(police_brutality_data)
            for word in brut_words:
                xvals.append(word[0])
                yvals.append(word[1])
            bar_data = go.Bar(x=xvals, y=yvals)
            basic_layout = go.Layout(title="Ten Most Common Words in 'Police Brutality' Query")
            fig=go.Figure(data=bar_data, layout=basic_layout)
            fig.show()
            xvals.clear()
            yvals.clear()
        elif query == 'police misconduct':
            misconduct_words = split_and_filter(police_misconduct_data)
            for word in misconduct_words:
                xvals.append(word[0])
                yvals.append(word[1])
            bar_data = go.Bar(x=xvals, y=yvals)
            basic_layout = go.Layout(title="Ten Most Common Words in 'Police Misconduct' Query")
            fig=go.Figure(data=bar_data, layout=basic_layout)
            fig.show()
            xvals.clear()
            yvals.clear()

if __name__ == '__main__':
    main()