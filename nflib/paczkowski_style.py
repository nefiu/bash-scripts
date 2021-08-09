'''
Utility functions for standardized formatting in Jupyter Notebook taken from 
"Introduction to Business Analytics: Using Python for Better Business Decisions" by Walter R. Paczkowski, Ph.D. (walt@dataanalyticscorp.com)
'''
##
## Default formats
##
bold = '\033[1m'
normal = '\033[0m'
def boldprt( s ):
    """
    Print text in bold and the return to normal.
    
    Args:
        s = string.
    """
    print( bold + s + normal )
##
def df_size( df ):
    """
    Display DataFrame size as nice output: rows and columns.
    
    Args:
        df: DataFrame handle.
    """
    data = { 'Count': [ df.shape[ 0 ], df.shape[ 1 ] ] }
    idx = [ 'Number of Rows', 'Number of Columns' ]
    display( pd.DataFrame( data, index = idx ).style.set_caption( 'DataFrame Dimensions' ).\
            set_table_styles( tbl_styles ) )
##
def footer():
    """
    Footer for graphs.  Display base and sample size.
    
    Args:
        None.  Assumes footer statement is defined as base = 'XXX'.
    """
    ax.annotate( base, ( 0, 0 ), ( 0, -0.3 ), xycoords = 'axes fraction' )
##
def tick_labels( tick ):
    """
    Modify graph ticks.
    
    Args:
        tick: axis x or y (lowercase).
    """
    if tick == 'y':
        vals = ax.get_yticks()
        ax.set_yticklabels( format.format( x ) for x in vals )
    else:
        vals = ax.get_xticks()
        ax.set_xticklabels( format.format( x ) for x in vals )
##
def leg( ax, ttl = None ):
    """
    Standardize location of legends.
    
    Args:
        ax: ax handle for graph.
        ttl: legend title.
    """
    ax.legend( title = ttl, loc = 'upper right', frameon = False, bbox_to_anchor=(1.25, 1.0) )
##
def mvReport( df ):
    """
    Calculate and display missing value report.
    Use sidetable package accessor stb.
    
    Args:
        df: dataFrame handle.
    """
    x = df.stb.missing( )
    ##
    ## Reorder columns and capitalize
    ##
    cols = [ 'total', 'missing', 'percent' ]
    x = x[ cols ]
    x.columns = x.columns.str.capitalize()
    ##
    ## Display
    ##
    base = 'Base: n = ' + str( df.shape[ 0 ] )
    fmt_dict = { 'Missing':'{:,.0f}', 'Total':'{:,.0f}', 'Percent':'{:.3}%' }
    display( x.style.set_caption( 'Missing Value Report').\
        format( fmt_dict ).set_table_styles( tbl_styles ) )
    print( base )
##
## Default formats
##
font_title = 20
format = '{:0.1%}'
format_dollar = '${:,.2f}'
p_value = '{:0.4f}'
##
## DataFrame styles
##
tbl_styles = [ {
    'selector': 'caption',
    'props': [
        ('color', 'darkblue'),
        ('font-size', '18px')
    ] } ]