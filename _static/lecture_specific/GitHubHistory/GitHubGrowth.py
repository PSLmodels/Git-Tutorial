'''
This script creates the time series plot of GitHub's growth in terms of users
and repositories since 2008. To execute, navigate in your terminal to the
directory "Git-Tutorial/book/_static/lecture_specific/GitHubHistory/" in this
repository and execute the Python script "python GitHubGrowth.py".
'''

# Import packages
import pandas as pd
import numpy as np
import os
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import (LinearAxis, Range1d, ColumnDataSource, CDSView,
                          BooleanFilter, Title, Legend)

# Read in data
cur_path = os.path.split(os.path.abspath(__file__))[0]
filename = 'GitGrowth.csv'
data_file_path = os.path.join(cur_path, filename)
github_df = pd.read_csv(data_file_path,
                        names=['date', 'users', 'unique_pub_repos',
                               'repos_forked_once', 'orgs', 'merged_prs',
                               'total_repos'],
                        parse_dates=['date'], skiprows=3, na_values=['.'])

github_growth_df = github_df[['date', 'users', 'total_repos']]

# Create two separate DataFrames for the repos and users data
github_growth_repos_df = \
    github_growth_df[['date', 'total_repos']].dropna(how='any')
github_growth_users_df = github_growth_df[['date', 'users']].dropna(how='any')

# Create list of dates in the original data points
date_all_list_str = github_growth_df['date'].dt.strftime('%Y-%m-%d').tolist()
date_repos_list = \
    github_growth_repos_df['date'].dt.strftime('%Y-%m-%d').tolist()
date_users_list = \
    github_growth_users_df['date'].dt.strftime('%Y-%m-%d').tolist()

# Add all days in range then interpolate data with cubic spline
days_df = \
    pd.DataFrame(pd.date_range(date_all_list_str[0], date_all_list_str[-1],
                               freq='D'), columns=['date'])
github_growth_interp_df = pd.merge(github_growth_df, days_df, left_on='date',
                                   right_on='date', how='outer')
github_growth_interp_df = github_growth_interp_df.sort_values(by='date')
github_growth_interp_df = github_growth_interp_df.reset_index(drop=True)
github_growth_interp_df['users'] = \
    github_growth_interp_df['users'].interpolate(method='cubic')
github_growth_interp_df['total_repos'] = \
    github_growth_interp_df['total_repos'].interpolate(method='cubic')
num_obs = github_growth_interp_df.shape[0]
github_growth_interp_df['date_index'] = pd.Series(range(0, num_obs))

# Create ColumnDataSource object
github_growth_interp_cds = ColumnDataSource(github_growth_interp_df)
# Create CDSViews objects
repos_booleans = []
users_booleans = []
date_all_list_ind = []
for row_ind in range(num_obs):
    date_str = \
        github_growth_interp_df['date'].iloc[row_ind].strftime('%Y-%m-%d')
    if date_str in date_repos_list:
        repos_booleans.append(True)
    else:
        repos_booleans.append(False)
    if date_str in date_users_list:
        users_booleans.append(True)
    else:
        users_booleans.append(False)
    if date_str in date_all_list_str:
        date_all_list_ind.append(int(
            github_growth_interp_df['date_index'].iloc[row_ind]))

repos_view = CDSView(source=github_growth_interp_cds,
                     filters=[BooleanFilter(repos_booleans)])
users_view = CDSView(source=github_growth_interp_cds,
                     filters=[BooleanFilter(users_booleans)])

# Create Bokeh plot of GitHub growth in users and repositories since 2008
fig_title = 'GitHub growth in users and repositories since 2008'
filename = ('GitHubGrowth.html')
output_file(filename, title=fig_title)

# # Format the tooltip
# repos_tooltips = [('Date', '@date{%F}'), ('Total repos', '$total_repos{0.}')]
# users_tooltips = [('Date', '@date{%F}'), ('Total users', '$users{0.}')]

fig_buffer_pct = 0.07  # Percent of data range to show extra above and below
fig = figure(plot_height=450,
             plot_width=900,
             x_axis_label='Date',
             y_axis_label='Total users and repositories',
             #  y_range=(min_main_val - fig_buffer_pct * datarange_main_vals,
             #           max_main_val + fig_buffer_pct * datarange_main_vals),
             #  x_range=((-np.round(bkwd_mths_main * 364.25 / 12) -
             #           fig_buffer_pct * datarange_main_days),
             #           (np.round(frwd_mths_main * 364.25 / 12) +
             #           fig_buffer_pct * datarange_main_days)),
             tools=['save', 'zoom_in', 'zoom_out', 'box_zoom', 'undo', 'redo',
                    'reset', 'help'],
             toolbar_location='right'
            )
fig.title.text_font_size = '18pt'
fig.toolbar.logo = None

# Set left-axis data and range
y1_var = 'total_repos'
y1_min = github_growth_interp_df[y1_var].min()
y1_max = github_growth_interp_df[y1_var].max()
y1_range_minmax = y1_max - y1_min
tot_repos_line = \
    fig.line(x='date_index', y='total_repos', source=github_growth_interp_cds,
             color='blue', line_width=2, alpha=0.7)
tot_repos_scatter = \
    fig.circle(x='date_index', y='total_repos',
               source=github_growth_interp_cds, view=repos_view, size=7,
               color='blue')
# fig.y_axis_label = 'Total repositories'
fig.y_range = Range1d(y1_min - fig_buffer_pct * y1_range_minmax,
                      y1_max + fig_buffer_pct * y1_range_minmax)

# Set right-axis data and range
y2_var = 'users'
y2_min = github_growth_interp_df[y2_var].min()
y2_max = github_growth_interp_df[y2_var].max()
y2_range_minmax = y2_max - y2_min
users_line = \
    fig.line(x='date_index', y='users', source=github_growth_interp_cds,
             color='green', line_width=2, alpha=0.7)
users_scatter = \
    fig.circle(x='date_index', y='users',
               source=github_growth_interp_cds, view=users_view, size=7,
               color='green')
# fig.y_axis_label = 'Users'
fig.y_range = Range1d(y1_min - fig_buffer_pct * y1_range_minmax,
                      y1_max + fig_buffer_pct * y1_range_minmax)

# Create the tick marks for the x-axis and set x-axis labels
date_label_dict = dict(zip(date_all_list_ind, date_all_list_str))
fig.xaxis.ticker = date_all_list_ind
fig.xaxis.major_label_overrides = date_label_dict

# Rotate the x-axis labels by 45 degrees or pi / 4
fig.xaxis.major_label_orientation = np.pi / 4

# Create tick marks for teh y-axis and set y_axis labels
yaxis_list_num = [0, 20000000, 40000000, 60000000, 80000000, 100000000,
                  120000000, 140000000]
yaxis_list_str = ['0', '20 mil', '40 mil', '60 mil', '80 mil', '100 mil',
                  '120 mil', '140 mil']
yaxis_label_dict = dict(zip(yaxis_list_num, yaxis_list_str))
fig.yaxis.ticker = yaxis_list_num
fig.yaxis.major_label_overrides = yaxis_label_dict

# Add legend
legend = Legend(items=[('Total repositories (data)', [tot_repos_scatter]),
                       ('Total repositories (interpolated)', [tot_repos_line]),
                       ('Total users (data)', [users_scatter]),
                       ('Total users (interpolated)', [users_line])],
                location='top_center')
fig.add_layout(legend)

# Add title and subtitle to the plot
fig.add_layout(Title(text=fig_title, text_font_style='bold',
                     text_font_size='18pt', align='center'), 'above')

# # Add source text below figure
# fig.add_layout(Title(text='Source: Richard W. Evans (@RickEcon), ' +
#                           'Data come from 2013-2019 State of the Octoverse ' +
#                           'reports (https://octoverse.github.com/) as well ' +
#                           'as Wikipedia "GitHub" and "Timeline of GitHub" ' +
#                           'articles.',
#                      align='left',
#                      text_font_size='3mm',
#                      text_font_style='italic'),
#                 'below')

# # Add the HoverTool to the figure
# fig.add_tools(HoverTool(renderers=[repos_hover_glyph], tooltips=repos_tooltips,
#                         toggleable=False, formatters={'@date': 'datetime'}))

show(fig)
