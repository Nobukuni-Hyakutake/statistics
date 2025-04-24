# 下記のエラーが出て保存できない
#ValueError: Vega to PNG conversion failed:
#SVG data parsing failed cause nodes limit reached

import polars as pl
import numpy as np
import altair as alt
alt.data_transformers.enable("vegafusion")
alt.data_transformers.disable_max_rows()

n = 1000000
s = np.random.normal(0, 1, n)
h = np.random.normal(0, 1, n)
df = pl.DataFrame({"value": s, "h": h}).with_columns(
    pl.when(pl.col("h") > 0)
    .then(pl.lit("high"))
    .otherwise(pl.lit("low"))
    .alias("high_low"),
    pl.lit(0.5).alias("a"),
)

chart1 = (
    alt.Chart().mark_bar().encode(alt.X("value").bin(), y=alt.Y("count()", title="Pcs"))
)

chart2 = alt.Chart().mark_rule().encode(x="a")

chart = (chart1 + chart2).facet(row="high_low", data=df)

chart.save("./trial/altair_histogram_trial16.png")
