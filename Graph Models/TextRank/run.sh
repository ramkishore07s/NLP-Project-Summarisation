filename="$1"
tag_rel_path="../"$filename

cd stanford-postagger-full-2015-04-20
./stanford-postagger.sh models/english-left3words-distsim.tagger $tag_rel_path > ../tagged.txt
cd ..
python3 tokenizer.py
python3 ngrams_finder.py
python3 sentence_ex.py $filename
python3 eval.py $filename