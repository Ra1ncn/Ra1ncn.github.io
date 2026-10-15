# WEBrick <= 1.9.2 treats a matching If-Range as 304 Not Modified.
# Chrome needs 206 with the requested bytes when seeking through an MP4.
# This only adjusts the development server; production builds need no plugin.
if Jekyll.env == "development"
  require "webrick"

  if Gem::Version.new(WEBrick::VERSION) <= Gem::Version.new("1.9.2")
    module LocalVideoRanges
      def do_GET(req, res)
        return super unless File.extname(@local_path).downcase == ".mp4" &&
                            req["range"] && req["if-range"]

        range_header = req.header["range"]
        validator_header = req.header["if-range"]
        stat = File.stat(@local_path)
        etag = format("%x-%x-%x", stat.ino, stat.size, stat.mtime.to_i)
        validator = req["if-range"]
        matches = validator == etag || validator == %Q("#{etag}")
        unless matches
          begin
            matches = Time.httpdate(validator).to_i >= stat.mtime.to_i
          rescue ArgumentError
            matches = false
          end
        end

        # A matching validator keeps Range (206); a stale one sends the full
        # representation (200). Other conditional headers keep normal behavior.
        req.header.delete("if-range")
        req.header.delete("range") unless matches
        begin
          super
        ensure
          req.header["range"] = range_header
          req.header["if-range"] = validator_header
        end
      end
    end

    WEBrick::HTTPServlet::DefaultFileHandler.prepend(LocalVideoRanges)
  end
end
