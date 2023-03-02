#!/usr/bin/env ruby

from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flag(.*?)\]/)
puts [from, to, flags].join(',')
