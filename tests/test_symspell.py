import symspell_rs as model
def test_models():
    # import time
    # print(SymspellPy(max_distance=2,prefix_length=7,count_threshold=1))
    sym_spell = model.SymspellPy(max_distance=2,prefix_length=7,count_threshold=1)

    if not sym_spell.load_dictionary("./data/frequency_dictionary_en_82_765.txt",0,1," "):
        print("Not Found")
    else:
        print("Found")
    # start = time.time()
    suggestions = sym_spell.lookup_compound("whereis th elove hehad dated forImuch of thepast who couqdn'tread in sixtgrade and ins pired him",2)
    # # # suggestions = sym_spell.lookup("roet",0,2)
    # # # words = sym_spell.get_words()
    # # # print(len(words))
    for cand in suggestions:
        print(f"Term->{cand.term} \n Distance->{cand.distance} \n Count->{cand.count}")

    seg_obj = sym_spell.word_segmentation("whereisthelove",2)
    print(f"String->{seg_obj.segmented_string} \n Distance->{seg_obj.distance_sum} \n Prob_Log_Sum->{seg_obj.prob_log_sum}")
    # print(time.time()-start)
    assert 1 == 1
test_models()