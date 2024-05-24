import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

csv_route='C:/maliciousweb/df_ex02.csv'

# CSV 파일 읽기
edges_df = pd.read_csv(csv_route, encoding='utf-8-sig')

edges = list(edges_df[['start', 'inner_url']].itertuples(index=False, name=None))

G = nx.DiGraph()
G.add_edges_from(edges)

# 네트워크 그리기
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

#페이지랭크 계산
pr = nx.pagerank(G,alpha=1)
print(pr)

# PageRank 상위 10개 노드 출력
top_10 = sorted(pr.items(), key=lambda item: item[1], reverse=True)[:10]
print("Top 10 PageRank nodes:")
for node, score in top_10:
    print(f"{node}: {score:.6f}")
