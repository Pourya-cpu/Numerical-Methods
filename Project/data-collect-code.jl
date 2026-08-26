using HTTP, JSON, Dates, DataFrames, CSV

function date_to_timestamp(date_str)
    date_time = DateTime(date_str, "yyyy-mm-dd HH:MM:SS")
    return round(Int, datetime2unix(date_time) * 1000)
end

function timestamp_to_date(timestamp_ms)
    return unix2datetime(timestamp_ms / 1000)  
end

function collect_bitcoin_rate(Symbol, interval, limit, start_time=nothing, end_time=nothing)
    
end

